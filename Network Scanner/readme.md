# **Network Scanner** 🖥️🔍

This Python script is designed to scan a network and discover devices connected to it using the **ARP (Address Resolution Protocol)**. It sends ARP requests to a specified IP range and retrieves the IP and MAC addresses of devices in the network.

> **⚠️ WARNING: Use responsibly**  
> This script is intended for educational purposes and authorized network monitoring only. Always ensure you have proper authorization before using this script.

---

## **📜 Overview**

The script works by sending ARP requests to all IP addresses in a given range (e.g., `10.0.2.1/24`). It listens for ARP responses to discover devices on the network. Each response includes the IP and MAC address of a device.

This script can be useful for network administrators to discover devices in their network or for penetration testers to scan a local network.

---

## **🔧 Features**

- **Network Scanning**: Sends ARP requests to a specified IP range and detects live devices.
- **MAC and IP Retrieval**: Retrieves both the IP and MAC addresses of the devices on the network.
- **User-friendly Output**: Outputs a list of devices with their IP and MAC addresses.

---

## **⚙️ Installation**

### 1. Clone the repository:
```bash
git clone https://github.com/phoenix-2211/Network-Scanner.git
