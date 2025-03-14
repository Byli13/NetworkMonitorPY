"""
Module for managing and displaying packet statistics.
"""

import threading
import time
import logging
from collections import Counter

# Global counter for protocol statistics
packet_counter = Counter()
counter_lock = threading.Lock()

def update_packet_count(protocol):
    """
    Thread-safe update of the packet counter.
    """
    with counter_lock:
        packet_counter[protocol] += 1

class StatsManager:
    def __init__(self, interval=5):
        self.interval = interval
        self._stop_event = threading.Event()
        self.thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        while not self._stop_event.is_set():
            time.sleep(self.interval)
            self.print_stats()

    def print_stats(self):
        with counter_lock:
            stats_snapshot = dict(packet_counter)
        logging.info("Packet Statistics:")
        for protocol, count in stats_snapshot.items():
            logging.info("  %s: %d", protocol, count)
        logging.info("-" * 40)

    def start(self):
        self.thread.start()

    def stop(self):
        self._stop_event.set()
        self.thread.join()
