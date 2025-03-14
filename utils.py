"""
Utility module for the Advanced Network Monitor.
Provides helper functions such as CSV logging of statistics.
"""

import csv
import time

def log_stats_to_csv(filename, stats_dict):
    """
    Append the current statistics to a CSV file with a timestamp.
    """
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['timestamp'] + list(stats_dict.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write header only if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
        row = {'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')}
        row.update(stats_dict)
        writer.writerow(row)
