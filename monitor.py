"""
Module for network packet monitoring using Scapy.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP
from stats import update_packet_count
import logging

def process_packet(packet):
    """
    Process each captured packet and update protocol counts.
    """
    if packet.haslayer(IP):
        if packet.haslayer(TCP):
            update_packet_count('TCP')
        elif packet.haslayer(UDP):
            update_packet_count('UDP')
        elif packet.haslayer(ICMP):
            update_packet_count('ICMP')
        else:
            update_packet_count('Other_IP')
    else:
        update_packet_count('Non_IP')

def start_sniffing(filter_str="ip", iface=None):
    """
    Start sniffing network packets based on a BPF filter.
    """
    logging.info("Starting packet sniffing with filter: %s", filter_str)
    sniff(filter=filter_str, prn=process_packet, iface=iface)
