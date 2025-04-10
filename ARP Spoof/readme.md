# ARP Spoofing Script

This Python script is used for performing **ARP (Address Resolution Protocol)** spoofing attacks. ARP spoofing allows an attacker to intercept the traffic between two devices on the same local network by associating their **MAC address** with the **IP address** of another device.

**WARNING: This script is for educational purposes only. Use it only in a controlled environment, such as penetration testing or network security research, with proper authorization.**

---

## 🌐 **ARP Spoofing (ARP Poisoning)**

ARP Spoofing, also known as **ARP Poisoning**, is a technique used to manipulate the ARP cache of devices within a local network. The attacker can impersonate another device, redirecting network traffic, intercepting communication, or causing a **Denial of Service (DoS)** attack. 

This script helps perform ARP spoofing on a network by continuously sending fake ARP replies to target devices.

### ⚙️ **How ARP Spoofing Works:**
1. **ARP Requests & Responses:**
   - Devices communicate on a network using ARP to map **IP addresses** to **MAC addresses**. When a device wants to reach another device on the network, it sends out an **ARP request** to know the MAC address corresponding to a given IP address.
   
2. **The Spoofing Attack:**
   - In ARP Spoofing, the attacker sends **fake ARP messages** to the network, associating their **MAC address** with the **IP address** of a legitimate device (like the **gateway/router**). This misleads other devices on the network into thinking the attacker’s device is the target device.

3. **Redirecting Traffic:**
   - Once the attacker’s **MAC address** is linked to a valid **IP address** (e.g., the gateway’s IP), network traffic intended for that IP is now sent to the attacker’s machine. The attacker can:
     - **Intercept** communication between devices.
     - **Modify** or **inject malicious data** into the traffic.
     - **Monitor** or even **alter** sensitive information such as passwords, financial transactions, and more.

4. **ARP Cache Poisoning:**
   - With the network's ARP table poisoned, the attacker controls the flow of data between devices. This can lead to **service disruption**, or in some cases, **complete network downtime**.

5. **Restoring Normalcy:**
   - After the attack, the attacker can **restore the ARP tables** by sending **correct ARP replies**, ensuring that network devices can resume normal operation.

---

## Features
- **Spoofing functionality**: Continuously send ARP packets to impersonate another device on the network.
- **ARP table restoration**: When the script is interrupted, it restores the ARP tables to the original state, minimizing network disruption.
- **Customizable IP addresses**: Specify any target device and gateway to carry out the attack.

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/phoenix-2211/ARP-Spoofing.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd ARP-Spoofing
    ```

3. **Install the required dependencies**:
    This script uses the `scapy` library, which can be installed via:
    ```bash
    pip install scapy
    ```

4. **Run the script**:
    ```bash
    python3 arp_spoof.py
    ```

---

## Example Usage

Run the ARP spoofing script using the following command:
```bash
python3 arp_spoof.py
