#!/usr/bin/python3
# coding=utf-8
from ipwhois import IPWhois
import socket
import time


def connection_speed(hostname: str) -> "float|None":
    ip_address = socket.gethostbyname(hostname)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        start_time = time.time()
        result = sock.connect_ex((ip_address, 80))
        end_time = time.time()
        sock.close()
        return end_time - start_time if result == 0 else None


def get_domain_location(domain: str) -> str:
    try:
        ip = socket.gethostbyname(domain)
        obj = IPWhois(ip, timeout=1)
        results = obj.lookup_rdap(retry_count=0)
        return results['asn_country_code']
    except Exception:
        return 'UNKOWN'
