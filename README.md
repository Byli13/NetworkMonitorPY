# Network Monitor using Python and Scapy

This project is a simple network monitor that captures IP packets and displays real-time protocol statistics using Python and Scapy.

## Features
- **Real-time Packet Capture:** Listens for IP packets on the network.
- **Protocol Classification:** Differentiates between TCP, UDP, and other IP-based packets.
- **Live Statistics:** Displays protocol counts every 5 seconds.

## Requirements
- Python 3.6+
- Scapy (see `requirements.txt`)
- libpcap development headers (e.g. `sudo apt-get install libpcap-dev` on Debian/Ubuntu)

## Installation & Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Monitor (requires root privileges):**
   ```bash
   sudo python main.py --interface <your_interface>
   ```

Captured packet statistics will be logged every few seconds. Press `Ctrl+C` to stop the monitor.

