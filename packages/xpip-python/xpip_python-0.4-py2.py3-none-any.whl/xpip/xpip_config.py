#!/usr/bin/python3
# coding=utf-8
import os
import toml

URL_PROG = "https://github.com/zoumingzhe/xpip-python"
DIR_CONF = f"{os.path.dirname(__file__)}/config"


def load(path: str) -> dict:
    with open(path, 'r') as f:
        return toml.load(f)


def dump(path: str, object: dict) -> str:
    with open(path, 'w') as f:
        return toml.dump(object, f)
