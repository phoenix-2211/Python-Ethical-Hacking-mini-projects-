# 🛡️ **ARP Spoofing Detection Script** 🛡️

This Python script is designed to detect **ARP Spoofing** attacks in a local network. ARP spoofing is a malicious technique used by attackers to intercept and manipulate network traffic. This script listens to ARP packets and checks for discrepancies in MAC addresses, alerting the user if a potential attack is detected.

> **⚠️ WARNING: For educational purposes only.**  
> Always use in a controlled environment, such as penetration testing or network security research, **with explicit authorization**.

---

## **📜 Overview**

**ARP Spoofing** (or ARP poisoning) involves an attacker sending false ARP messages to associate their MAC address with the IP address of another device on the network. This script listens for ARP packets, checks for any anomalies in the MAC addresses, and alerts if a spoofing attempt is detected.

---

## **🔧 Features**

- **Packet Sniffing**: Monitors ARP packets on a specified network interface.
- **Attack Detection**: Detects discrepancies in MAC addresses, alerting the user if a spoofing attempt is identified.
- **Continuous Monitoring**: Runs indefinitely, listening for potential ARP spoofing attacks in real-time.

---

## **⚙️ Installation**

### 1. Clone the repository:
```bash
git clone https://github.com/phoenix-2211/ARP-Spoofing-Detection.git
