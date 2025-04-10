# Keylogger Script

This Python-based Keylogger script is a tool that records keystrokes made on the system and sends them to a specified email at user-defined intervals. The script utilizes the powerful `pynput` library to capture keyboard events and `smtplib` to send emails with the logged data. 

This tool is mainly designed for **educational purposes**. It demonstrates the basics of keystroke logging and email sending, but must **only be used in controlled environments** with explicit permission. Unauthorized use of this tool is **illegal** and unethical.

---

## ⚠️ **Important Warning**

This script is **not** intended for malicious use. **Only use this tool on systems that you have explicit permission to monitor**, such as in penetration testing, ethical hacking, or security research. Unauthorized use of keyloggers is a violation of privacy and illegal.

---

## ✨ **Overview**

The script allows you to monitor keystrokes on the system. Once the keys are captured, they are sent to your **designated email address** at a fixed interval. This tool can be helpful in educational scenarios where understanding how keylogging works is essential. 

### 🛠 **Key Features**:
- **Keystroke Logging**: Logs every keypress on the system.
- **Email Integration**: Sends the logged data to an email address.
- **Time-based Reporting**: Sends the captured data at customizable time intervals (e.g., every 60 seconds).
- **Simple Setup**: Just input your email and password, and you're good to go!

---

# Keylogger Script

This Python script logs keystrokes and sends the captured data to a specified email address. It is intended for **educational purposes only** and must be used responsibly and ethically.

---

## ⚠️ **Important Warning**

**Unauthorized use** of this keylogger is **illegal** and unethical. Only use it on systems you own or have explicit permission to monitor. This tool is designed for **ethical hacking** and **security research** in controlled environments.

---

## 💻 **Setup & Configuration**

To use the script, you need to provide your **email credentials** (email address and password). This is required so the script can send the logged keystrokes to your inbox.

### 🛠 **Steps to Configure Your Email**:

1. Open the **Keylogger script**.
2. Locate the section where email credentials are needed:
    ```python
    keylogger = Keylogger(time_interval=60, email="youremail@gmail.com", password="yourpassword")
    ```
3. **Replace** the placeholders:
    - `youremail@gmail.com`: Replace with your **Gmail address**.
    - `yourpassword`: Replace with your **Gmail password** (or use an **App Password** if 2FA is enabled).
    
4. Optionally, you can use **environment variables** for better security instead of hardcoding your credentials.

---

## 🔑 **Important Notes on Email Configuration**

- **Gmail Security**: If you are using Gmail, make sure that your account allows access to less secure apps or generate an **App Password** if you have **two-factor authentication (2FA)** enabled.
    - For more details on App Passwords: [Google Account Security](https://support.google.com/accounts/answer/185833?hl=en)
    
- **Never share your email credentials** in public repositories. Use environment variables or other secure methods to handle sensitive information.

---

## 💡 **Example Usage**:

After configuring the email credentials, run the script as follows:
```python
keylogger = Keylogger(time_interval=60, email="your_email@gmail.com", password="your_password")
keylogger.start()
