#!/usr/bin/python3
# coding=utf-8
from enum import Enum, unique
from typing import List

from ping3 import ping

# import time


@unique
class ErrorCode(Enum):
    BaseException = 230316
    KeyboardInterrupt = 230317


def ping_second(address: str, count: int = 3, timeout: int = 1) -> float:
    delay: List[float] = []

    if count < 1:
        count = 1

    if timeout < 1:
        timeout = 1

    for i in range(count):
        t = ping(address, seq=i, timeout=timeout)
        # False on error and None on timeout.
        if t is None:
            return float(-timeout)
        if t is False:
            return 0.0
        delay.append(t)

    return sum(delay) / len(delay)
