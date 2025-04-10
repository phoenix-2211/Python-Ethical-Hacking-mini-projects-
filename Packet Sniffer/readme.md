# **HTTP Packet Sniffer** 🌐📡

This Python script is designed to sniff HTTP packets on a network and capture sensitive data, including URLs and login credentials, such as usernames and passwords. The script uses **Scapy** to listen for HTTP requests and extract information from them.

> **⚠️ WARNING: Ethical Use Only**  
> This script is intended for educational purposes and authorized network monitoring only. Always ensure you have proper authorization before using this script.

---

## **📜 Overview**

This script listens for HTTP packets on a specified network interface. It captures the requested URLs and checks if any login information (such as usernames and passwords) is transmitted in the HTTP packets. 

**NOTE**: This script works by sniffing traffic on a network that is passing through the device running the script. It does **not** work for encrypted HTTPS traffic.

---

## **🔧 Features**

- **HTTP Sniffing**: Captures HTTP packets and extracts URLs.
- **Login Detection**: Looks for potential usernames and passwords in the HTTP request data.
- **Real-time Monitoring**: Continuously monitors the network interface for HTTP traffic.

---

## **⚙️ Installation**

### 1. Clone the repository:
```bash
git clone https://github.com/phoenix-2211/HTTP-Packet-Sniffer.git
