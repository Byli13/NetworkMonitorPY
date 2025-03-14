
# !/usr/bin/env python3
"""
Advanced Network Monitor using Python and Scapy

Entry point of the project.
"""

import argparse
import logging
import threading
import time
from monitor import start_sniffing
from stats import StatsManager


def setup_logging(log_file):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Advanced Network Monitor using Python and Scapy"
    )
    parser.add_argument('--interface', type=str, default=None,
                        help='Network interface to monitor')
    parser.add_argument('--log', type=str, default='network_monitor.log',
                        help='Log file name')
    parser.add_argument('--stats-interval', type=int, default=5,
                        help='Interval in seconds to print stats')
    parser.add_argument('--filter', type=str, default="ip",
                        help='BPF filter for packet sniffing')
    return parser.parse_args()


def main():
    args = parse_arguments()
    setup_logging(args.log)
    logging.info("Starting Advanced Network Monitor")

    # Start the statistics manager in a separate thread
    stats_manager = StatsManager(interval=args.stats_interval)
    stats_manager.start()

    try:
        # Start packet sniffing on the specified interface and filter
        start_sniffing(filter_str=args.filter, iface=args.interface)
    except KeyboardInterrupt:
        logging.info("Stopping Network Monitor...")
    finally:
        stats_manager.stop()


if __name__ == "__main__":
    main()
