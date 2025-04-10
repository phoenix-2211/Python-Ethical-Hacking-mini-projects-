# MAC Address Changer Script

## Overview
This Python script allows you to change the **MAC (Media Access Control)** address of a network interface on your system. It provides a simple way to modify your network adapter's MAC address using Python.

### Features:
- Change the MAC address of any network interface.
- Read the current MAC address of an interface.
- Easy-to-use with command-line arguments for specifying the interface and new MAC address.

## Requirements
To run the script, you will need the following:
- Python 3.x
- Linux-based system (macOS or Ubuntu preferred)
- The `ifconfig` utility (commonly installed on most Linux-based systems)
  
## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/phoenix-2211/MAC-Address-Changer.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd MAC-Address-Changer
    ```

3. **Make sure you have Python 3 installed**:
    ```bash
    python3 --version
    ```

4. **Run the script** using the following command:
    ```bash
    python3 change_mac.py -i INTERFACE -m NEW_MAC_ADDRESS
    ```
    - Replace `INTERFACE` with your network interface (e.g., `eth0` or `wlan0`).
    - Replace `NEW_MAC_ADDRESS` with the new MAC address you want to set.

