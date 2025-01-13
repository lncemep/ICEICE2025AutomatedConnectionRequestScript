import time
import random
import logging
import pandas as pd
import os
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

CONFIG_FILE = "config.json"

if not os.path.exists(CONFIG_FILE):
    logging.error(f"Configuration file '{CONFIG_FILE}' not found.")
    exit(1)

with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
    try:
        config = json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Disassembly error '{CONFIG_FILE}': {e}")
        exit(1)

EVENT_URL = "https://event.clariongaming.com/event/ice-2025/person/RXZlbnRQZW9wbGVfMzU5NTAxOTY="
EMAIL_FOR_EVENT = config.get("login_email", "")
SENDER_NAME = config.get("sender_name")
PROXY_CONFIG = config.get("proxy", {})
EXCEL_FILE = "profiles.xlsx"
DEFAULT_MESSAGE = config.get("default_message", "")
SHEET_NAME = 0
CHROME_DRIVER_PATH = r"chromedriver-win64\chromedriver.exe"

if not EMAIL_FOR_EVENT:
    logging.error("Login Email is not specified in the configuration.")
    exit(1)

if not DEFAULT_MESSAGE:
    logging.error("The default message is not specified in the configuration.")
    exit(1)

def configure_proxy(options):
    proxy_host = PROXY_CONFIG.get("host", "")
    proxy_port = PROXY_CONFIG.get("port", "")

    proxy = f"http://{proxy_host}:{proxy_port}"
    options.add_argument(f'--proxy-server={proxy}')

    return options

def login_to_event(driver):
    """
    1) Open EVENT_URL
    2) Click “Accept All” (span[text()='Accept All']), if available
    3) Click “Username” (span[text()='Username']), if necessary
    4) Enter e-mail
    5) Click “Continue” (span[text()='Continue']), if necessary.
    6) Ask the user to manually enter the code (format XXX-XXX)
    7) Enter the code character by character
    8) Allow 3 seconds for the site to automatically log in
    """

    driver.get(EVENT_URL)

    """
    Pauses the program until the user confirms they have logged in via the proxy.
    """
    input("Please manually log in to the proxy (enter username and password), then press Enter to continue...")

    try:
        cookie_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'hAsOJc') and text()='Accept all']"))
        )
        cookie_btn.click()
        logging.info("Clicked 'Accept all' (cookies).")
    except Exception as e:
        logging.info(f"Cookie banner did not appear or did not find 'Accept all'. Error: {e}")

    try:
        user_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']"))
        )
        user_btn.click()
        logging.info("Clicked 'Log in'. Open the login form.")
    except Exception as e:
        logging.info(f"Did not find 'Log in' - the login form may already be visible. Error: {e}")

    try:
        email_input = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
        )
        email_input.clear()
        email_input.send_keys(EMAIL_FOR_EVENT)
        logging.info("We've got e-mail.")
    except Exception as e:
        logging.error(f"Couldn't find the e-mail field: {e}")
        return False

    try:
        continue_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue']"))
        )
        continue_btn.click()
        logging.info("Clicked 'Continue'. Wait for the user to receive the code.")
    except Exception as e:
        logging.error(f"Didn't find / didn't click 'Continue': {e}")
        return False

    print("Check your email and enter a code such as 'ABC-123':")
    code = input("Enter the code from the e-mail (format XXX-XXX): ").strip()
    digits = code.replace("-", "")
    if len(digits) != 6:
        logging.error(f"Incorrect code format '{code}'. Must be 6 characters after the hyphen is removed.")
        return False

    try:
        input_boxes = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='sc-41eb58bb-1 hILQrO']//input[@maxlength='1']")
            )
        )
        input_boxes = input_boxes[:6]

        for i, ch in enumerate(digits):
            input_boxes[i].click()
            input_boxes[i].clear()
            input_boxes[i].send_keys(ch)

        logging.info("The code is manually entered. Wait 3 seconds for auto-login....")
        time.sleep(3)
        return True

    except Exception as e:
        logging.error(f"Code entry error: {e}")
        return False

def open_connect_page(driver, url):
    """
    Goes to the page url and clicks “Connect” (span[text()='Connect']).
    """
    try:
        driver.get(url)
        connect_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Connect']"))
        )
        connect_button.click()
        logging.info(f"Clicked 'Connect' on the page {url}")
        return True
    except Exception as e:
        logging.error(f"Failed to press 'Connect' on {url}: {e}")
        return False

def send_message(driver, prospect_name):
    """
    He enters a message and clicks “Send connection request” (span[text()='Send connection request']).
    """
    try:
        message_box = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//textarea[contains(@placeholder, 'A connection request')]")
            )
        )
        custom_message = (
            DEFAULT_MESSAGE
            .replace("[Name of prospect]", prospect_name if prospect_name else "there")
            .replace("[Name of Profile]", SENDER_NAME)
        )
        message_box.clear()
        message_box.send_keys(custom_message)

        send_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='Send connection request']")
            )
        )
        send_button.click()

        logging.info("The message has been successfully sent.")
        return True
    except Exception as e:
        logging.error(f"Failed to send message: {e}")
        return False
    
def main():
    options = Options()
    options.add_argument("--start-maximized")
    options = configure_proxy(options)
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(30)

    try:
        logging.info("Open the site, click 'Accept All', 'Username', 'Continue', then wait for the code...")
        if not login_to_event(driver):
            logging.error("Failed to complete the login on the site.")
            return

        logging.info("You have successfully logged in to events.clariongaming.com!")

        try:
            df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
        except FileNotFoundError:
            logging.error(f"Excel file '{EXCEL_FILE}' not found.")
            return
        except ValueError as e:
            logging.error(f"Error when reading a sheet '{SHEET_NAME}': {e}")
            return

        if "Profile Link" not in df.columns or "Name" not in df.columns:
            logging.error("Excel should have 'Profile Link' and 'Name' columns.")
            return

        successful_sends = 0
        total_rows = len(df)

        for idx, row in df.iterrows():
            profile_link = str(row["Profile Link"]).strip()
            prospect_name = str(row["Name"]).strip()

            if not profile_link:
                logging.warning(f"String {idx}: 'Profile Link' is blank. Skip.")
                continue

            logging.info(f"({idx}) Follow the link: {profile_link}")
            if open_connect_page(driver, profile_link):
                if send_message(driver, prospect_name):
                    successful_sends += 1

            time.sleep(random.uniform(60, 120))

        logging.info(f"Script completed. Successfully sent {successful_sends} from {total_rows} requests.")
        print(f"Successfully dispatched {successful_sends} from {total_rows} requests.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
