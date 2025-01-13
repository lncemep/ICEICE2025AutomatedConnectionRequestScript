# ICE 2025 Automated Connection Request Script 🎉

Welcome to the **ICE 2025 Automated Connection Request** script! This tool streamlines the process of logging into the ICE 2025 event platform, navigating through user profiles, and sending personalized connection requests automatically. 🤖

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
  - [1. Create `config.json`](#1-create-configjson)
  - [2. Prepare `profiles.xlsx`](#2-prepare-profilesxlsx)
  - [3. Organize Multiple Accounts](#3-organize-multiple-accounts)
- [Usage](#usage)
- [Understanding the Script Workflow](#understanding-the-script-workflow)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Features

- **Automated Login**: Seamlessly logs into the ICE 2025 event platform.
- **Profile Navigation**: Reads profile links and names from an Excel file.
- **Personalized Messages**: Sends customized connection requests.
- **Proxy Support**: Configurable proxy settings for enhanced privacy.
- **Multiple Account Support**: Manage and run multiple accounts simultaneously.
- **Logging**: Detailed logs for monitoring and debugging.

## 🔧 Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System**: Windows, macOS, or Linux.
- **Python**: Version 3.7 or higher installed.
- **Chrome Browser**: Installed on your system.
- **ChromeDriver**: Compatible with your Chrome version.

## 🛠 Installation

Follow these steps to set up the environment and install necessary dependencies.

### 1. Install Python 🐍

If you haven't installed Python yet, follow these steps:

- **Download Python**: Visit the [official Python website](https://www.python.org/downloads/) and download the latest version for your operating system.

- **Install Python**:
  - **Windows**:
    - Run the installer.
    - **Important**: Check the box that says **"Add Python to PATH"**.
    - Click **"Install Now"**.
  - **macOS/Linux**:
    - Follow the installation instructions specific to your distribution.

- **Verify Installation**:
  - Open **Command Prompt** (Windows) or **Terminal** (macOS/Linux).
  - Type:
    ```bash
    python --version
    ```
    You should see the installed Python version.

### 2. Install Google Chrome 🖥️

Ensure you have Google Chrome installed. Download it from the [official website](https://www.google.com/chrome/).

### 3. Download ChromeDriver 🔧

ChromeDriver is required for Selenium to control Chrome.

- **Check Chrome Version**:
  - Open Chrome.
  - Click on the three dots in the top-right corner.
  - Go to **Help > About Google Chrome**.
  - Note the version number (e.g., 114.0.5735.90).

- **Download Matching ChromeDriver**:
  - Visit the [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/) page.
  - Download the version that matches your Chrome browser.

- **Extract ChromeDriver**:
  - Extract the downloaded file.
  - Move `chromedriver.exe` (Windows) or `chromedriver` (macOS/Linux) to a known directory, e.g., `chromedriver/`.

### 4. Clone the Repository 📥

Clone or download the script to your local machine.

```bash
git clone https://github.com/yourusername/ice2025-automated-connection.git
cd ice2025-automated-connection
```

### 5. Set Up a Virtual Environment (Optional but Recommended) 🛡️

Creating a virtual environment ensures that dependencies are managed separately.

- **Create Virtual Environment**:

  ```bash
  python -m venv venv
  ```

- **Activate Virtual Environment**:

  - **Windows**:
    ```bash
    venv\Scripts\activate
    ```
  - **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

### 6. Install Dependencies 📦

Install the required Python libraries using `pip`.

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Before running the script, set up the necessary configuration files.

### 1. Create `config.json` 📝

Create a `config.json` file in the project directory with the following structure:

```json
{
    "login_email": "your_email@example.com",
    "proxy": {
        "host": "proxy_host",
        "port": "proxy_port"
    },
    "sender_name": "Alex Jones",
    "default_message": "Hi [Name of prospect],\n\nAt Bankz, we specialize in supporting high-risk clients within the iGaming industry by offering customized banking and payment processing solutions for licensed companies.\n\nHere’s how Bankz can empower your operations:\n\n    • Multi-Currency IBAN Accounts: Seamlessly handle transactions in 39 currencies via SEPA, Faster Payments, and SWIFT.\n    • Visa Business Credit Cards: Issue unlimited cards compatible with Google and Apple Pay, with simple management through our dedicated mobile app.\n    • Crypto Liquidity: Easily convert cryptocurrency directly into your account.\n    • Payment Processing: Benefit from global coverage for cards and alternative payment methods (APMs) through a single, streamlined integration.\n    • We’re committed to delivering competitive pricing, swift onboarding, and tools designed to simplify financial management and optimize spending.\n\nTo better understand your needs, I’d recommend scheduling a face-to-face meeting during the ICE conference in Barcelona.\n\nYou can book an appointment using the link below:\n\nhttps://meetings.hubspot.com/avishai5/ice_barcelona\n\nOnce you’ve scheduled a time, please let me know so I can confirm on my end.\n\nLooking forward to connecting with you!\n\nTelegram : https://t.me/Bankz_Official\n\nBest Regards\n[Sender Name]\nhttps://www.Bankz.eu"
}
```

#### **Configuration Fields Explained**

- **`login_email`**: Your email address used to log into the ICE 2025 platform.
  
  ```json
  "login_email": "your_email@example.com"
  ```
  
- **`proxy`**: (Optional) Proxy settings to route your connection through a specific server. If you don't use a proxy, you can omit this section or leave the fields empty.
  
  ```json
  "proxy": {
      "host": "proxy_host",
      "port": "proxy_port"
  }
  ```
  
  - **`host`**: The hostname or IP address of your proxy server.
  - **`port`**: The port number your proxy server listens on.
  
- **`sender_name`**: Your name as it will appear in the sent messages.
  
  ```json
  "sender_name": "Alex Jones"
  ```
  
- **`default_message`**: The template message that will be sent as a connection request. You can personalize it using placeholders:
  
  - **`[Name of prospect]`**: Will be replaced with the prospect's name from `profiles.xlsx`.
  - **`[Sender Name]`**: Will be replaced with the `sender_name` from the configuration.
  
  ```json
  "default_message": "Hi [Name of prospect],\n\nAt Bankz, we specialize in supporting high-risk clients within the iGaming industry by offering customized banking and payment processing solutions for licensed companies.\n\n[...additional message content...]"
  ```

### 2. Prepare `profiles.xlsx` 📊

Create an Excel file named `profiles.xlsx` with the following columns:

- **Profile Link**: URL to the prospect's profile.
- **Name**: Name of the prospect.

Ensure the first row contains the headers.

> **Example**:

| Profile Link                             | Name        |
|------------------------------------------|-------------|
| https://event.clariongaming.com/profile1 | John Doe    |
| https://event.clariongaming.com/profile2 | Jane Smith  |

### 3. Organize Multiple Accounts 📁

To manage multiple accounts, follow these steps:

1. **Create Separate Folders**:
   
   For each account, create a separate folder containing its own configuration and necessary files.

   ```plaintext
   ice2025-automated-connection/
   ├── account1/
   │   ├── config.json
   │   ├── profiles.xlsx
   │   └── chromedriver.exe
   ├── account2/
   │   ├── config.json
   │   ├── profiles.xlsx
   │   └── chromedriver.exe
   └── requirements.txt
   ```

2. **Customize `config.json` for Each Account**:
   
   Each `config.json` should contain unique `login_email` and, if applicable, different proxy settings.

   ```json
   // account1/config.json
   {
       "login_email": "user1@example.com",
       "proxy": {
           "host": "proxy1_host",
           "port": "proxy1_port"
       },
       "sender_name": "Alex Jones",
       "default_message": "Hi [Name of prospect],\n\n[...additional message content...]"
   }
   
   // account2/config.json
   {
       "login_email": "user2@example.com",
       "proxy": {
           "host": "proxy2_host",
           "port": "proxy2_port"
       },
       "sender_name": "Maria Garcia",
       "default_message": "Hello [Name of prospect],\n\n[...additional message content...]"
   }
   ```

3. **Duplicate `profiles.xlsx` and `chromedriver`**:
   
   Ensure each account folder contains its own `profiles.xlsx` and `chromedriver` if necessary.

4. **Running Multiple Instances**:
   
   Open separate terminal instances for each account and navigate to their respective folders to run the script independently.

---

## 🚀 Usage

Follow these steps to run the script for a single account or multiple accounts.

### **Running for a Single Account**

1. **Open Command Prompt or Terminal** 🖥️

2. **Navigate to the Account Directory**:
   
   ```bash
   cd path/to/ice2025-automated-connection/account1
   ```

3. **Activate Virtual Environment** (if you set one up):
   
   - **Windows**:
     ```bash
     ../venv/Scripts/activate
     ```
   - **macOS/Linux**:
     ```bash
     source ../venv/bin/activate
     ```

4. **Run the Script**:
   
   ```bash
   python your_script_name.py
   ```
   
   > **Note**: Replace `your_script_name.py` with the actual name of your Python script.

5. **Follow On-Screen Prompts** 📢:
   
   - The script will open the Chrome browser and navigate to the ICE 2025 event URL.
   - **Manual Actions Required**:
     - **Login via Proxy**: If using a proxy, you may need to enter your proxy credentials.
     - **Verification Code**: After entering your email, you'll receive a verification code via email. Enter it when prompted.
     - **Press Enter**: After completing the manual steps, press Enter in the console to continue the automation.

6. **Monitor Logs** 📝:
   
   The script logs its progress and any errors to the console. Ensure to monitor these logs for successful execution.

### **Running Multiple Accounts Simultaneously**

1. **Open Multiple Terminal Instances**:
   
   Open separate Command Prompt or Terminal windows for each account.

2. **Navigate to Each Account Directory**:
   
   - **Terminal 1**:
     ```bash
     cd path/to/ice2025-automated-connection/account1
     ```
   - **Terminal 2**:
     ```bash
     cd path/to/ice2025-automated-connection/account2
     ```

3. **Activate Virtual Environment in Each Terminal** (if using one):
   
   - **Windows**:
     ```bash
     ../venv/Scripts/activate
     ```
   - **macOS/Linux**:
     ```bash
     source ../venv/bin/activate
     ```

4. **Run the Script in Each Terminal**:
   
   ```bash
   python your_script_name.py
   ```

5. **Follow On-Screen Prompts in Each Terminal**:
   
   Complete the manual login and verification steps for each account independently.

---

## 🧠 Understanding the Script Workflow

To effectively use the script, it's essential to understand where manual interactions are required. Here's a step-by-step explanation:

1. **Script Initialization**:
   
   - **Load Configurations**: The script reads `config.json` to retrieve login credentials, proxy settings, sender details, and the default message.
   - **Validate Configurations**: Ensures that `login_email` and `default_message` are provided.

2. **Proxy Configuration**:
   
   - If proxy settings are provided in `config.json`, Selenium is configured to route traffic through the specified proxy.

3. **Login Process**:
   
   - **Navigate to ICE 2025 URL**: The script opens the ICE 2025 event page.
   
   - **Manual Proxy Login**:
     - **Prompt**: 
       ```
       Please manually log in to the proxy (enter username and password), then press Enter to continue...
       ```
     - **Action**: Enter your proxy credentials in the browser and press Enter in the console to proceed.
   
   - **Handle Cookies**:
     - **Action**: If a cookie consent banner appears, the script will attempt to click "Accept all". If not found, it logs the information and continues.
   
   - **Initiate Login**:
     - **Action**: The script clicks the "Log in" button to open the login form.
   
   - **Enter Email**:
     - **Action**: The script enters the `login_email` from `config.json` into the email input field.
   
   - **Continue to Receive Verification Code**:
     - **Action**: Clicks the "Continue" button to receive a verification code via email.
   
   - **Manual Verification Code Entry**:
     - **Prompt**:
       ```
       Проверьте свою почту и введите код, например 'ABC-123':
       Введите код из письма (формат XXX-XXX):
       ```
     - **Action**: Check your email for the verification code, enter it in the console in the specified format (e.g., `ABC-123`), and press Enter.
   
   - **Automated Code Entry**:
     - The script inputs the verification code into the designated fields on the website.
     - **Wait**: Waits for 3 seconds to allow the site to automatically log in.

4. **Profile Processing**:
   
   - **Load `profiles.xlsx`**: Reads the Excel file containing profile links and names.
   
   - **Iterate Through Profiles**:
     - For each profile:
       - **Navigate to Profile Page**: Opens the profile URL.
       - **Click "Connect"**: Attempts to click the "Connect" button.
       - **Send Message**: Enters the personalized message into the message box and sends the connection request.
       - **Pause**: Waits for a random duration between 15 to 30 seconds to avoid spamming.

5. **Completion**:
   
   - **Log Results**: Outputs the number of successful connection requests sent out of the total.
   - **Close Browser**: Quits the Selenium WebDriver instance.

---

## 🛑 Troubleshooting

- **ChromeDriver Version Mismatch**:
  - **Issue**: Selenium cannot control Chrome if ChromeDriver version doesn't match the installed Chrome version.
  - **Solution**: Ensure ChromeDriver version matches your Chrome browser version. Download the correct version from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).

- **Missing Dependencies**:
  - **Issue**: Script fails due to missing Python libraries.
  - **Solution**: Re-run `pip install -r requirements.txt` to install all required dependencies.

- **Proxy Issues**:
  - **Issue**: Unable to connect via proxy.
  - **Solution**: Verify the proxy `host` and `port` in `config.json`. Ensure the proxy server is operational and credentials (if required) are correct.

- **Excel File Issues**:
  - **Issue**: `profiles.xlsx` not found or missing required columns.
  - **Solution**: Ensure `profiles.xlsx` exists in the account folder and contains the columns `Profile Link` and `Name`.

- **Permissions**:
  - **Issue**: Script lacks permissions to execute or access certain files.
  - **Solution**: Run the terminal with appropriate permissions or adjust file permissions accordingly.

- **Manual Steps Not Completed**:
  - **Issue**: Script awaits user input for proxy login or verification code.
  - **Solution**: Complete the manual steps in the browser and enter the required information in the console when prompted.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository** 🐸

2. **Create a Feature Branch**:
   
   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit Your Changes**:
   
   ```bash
   git commit -m "Add your message here"
   ```

4. **Push to the Branch**:
   
   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request** 🔄

Please ensure your contributions adhere to the project's coding standards and include appropriate documentation.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Happy automating! If you encounter any issues or have suggestions, feel free to reach out. 😊

---

# 4. Additional Files

### **`requirements.txt`**

Ensure this file is present in your root directory to manage dependencies.

```plaintext
selenium==4.9.1
pandas==1.5.3
```

---

# Summary

This `README.md` provides a step-by-step guide on installing, configuring, and using the **ICE 2025 Automated Connection Request** script. It includes detailed explanations of the configuration files, instructions for managing multiple accounts, and an in-depth understanding of the script's workflow, ensuring users can effectively utilize the automation tool with ease. 🌟

If you need further assistance or have specific questions about the script, feel free to ask! 😊
