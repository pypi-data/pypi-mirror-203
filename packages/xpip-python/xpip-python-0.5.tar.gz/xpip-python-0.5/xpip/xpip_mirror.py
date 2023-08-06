#!/usr/bin/python3
# coding=utf-8

import concurrent.futures
import socket
import sys
from errno import ENOENT
from typing import List, NamedTuple, Optional, Tuple
from urllib.parse import urlparse

from pip._internal.cli.main import main as pipcli
from tabulate import tabulate
from xarg import ArgSubParser, xarg

from .xpip_config import DIR_CONF, URL_PROG, dump, load
from .xpip_util import ErrorCode, ping_second

CONF_MIRRORS = f"{DIR_CONF}/mirrors.toml"


class MIRROR(NamedTuple):
    name: str
    url: str
    hostname: str
    address: str
    ping_ms: float


def get_mirror(name: str, url: str) -> MIRROR:
    try:
        hostname = urlparse(url).hostname
        address = socket.gethostbyname(hostname)
        ping_ms = ping_second(address, 10, 1) * 1000
    except TypeError:
        hostname = "ERROR"
        address = "UNKOWN"
        ping_ms = 0.0
    except socket.error:
        address = "UNKOWN"
        ping_ms = 0.0
    return MIRROR(name, url, hostname, address, ping_ms)


def get_mirrors(args) -> List[MIRROR]:
    mirrors: List[MIRROR] = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for key in args.mirrors:
            mirror: dict = args.mirrors[key]
            url: str = mirror['url']
            futures.append(executor.submit(get_mirror, key, url))
        for future in concurrent.futures.as_completed(futures):
            mirrors.append(future.result())
    # sort by speed
    mirrors.sort(key=lambda x: x.ping_ms, reverse=False)
    # move "timeout" values to the end of the list
    mirrors = sorted(mirrors, key=lambda x: x.ping_ms <= 0)
    return mirrors


def choice_mirror(mirrors: List[MIRROR], name: str = None) -> Optional[MIRROR]:
    if name is not None:
        for m in mirrors:
            if m[0] == name:
                return m
    elif len(mirrors) > 0 and mirrors[0].ping_ms > 0:
        # choice the best of mirror
        return mirrors[0]

    return None


def add_cmd_list(_arg: ArgSubParser):
    pass


def run_cmd_list(args) -> int:
    mirrors: List[MIRROR] = get_mirrors(args)
    # print table format
    tabular_data: List[Tuple[str, str, str, str]] = []
    for m in mirrors:
        _host = f"{m.hostname} ({m.address})"
        _ping = f"{m.ping_ms:.01f}" if m.ping_ms > 0 else "timeout"
        tabular_data.append((m.name, m.url, _host, _ping))
    table = tabulate(tabular_data,
                     headers=['name', 'URL', 'HOST', 'PING(ms)'],
                     floatfmt='.1f')  # tablefmt='simple'
    sys.stderr.write(f"{table}\n")
    sys.stdout.flush()
    # choice the best of mirror
    best = choice_mirror(mirrors)
    if best is not None:
        sys.stderr.write("\nSuggest using the installation command:\n"
                         f"pip install -i {best.url} <package-name>\n")
        sys.stdout.flush()
    return 0


def add_cmd_get(_arg: ArgSubParser):
    _arg.add_pos('name', type=str, nargs=1, help="specify name")


def run_cmd_get(args) -> int:
    _name = args.name
    if _name is not None and _name in args.mirrors:
        mirror: dict = args.mirrors[_name]
        sys.stderr.write(f"{mirror['url']}\n")
        sys.stdout.flush()
    return 0


def add_cmd_set(_arg: ArgSubParser):
    _arg.add_pos('name', type=str, nargs=1, help="specify name")
    _arg.add_pos('url', type=str, nargs=1, help="specify url")


def run_cmd_set(args) -> int:
    _name = args.name
    _url = args.url
    if _name is not None and _url is not None:
        mirror = {_name: {'url': _url}}
        args.mirrors.update(mirror)
        dump(args.config, args.mirrors)
    return 0


def add_cmd_now(_arg: ArgSubParser):
    pass


def run_cmd_now(args) -> int:
    pipcli("config get global.index-url".split())
    return 0


def add_cmd_choice(_arg: ArgSubParser):
    _arg.add_pos('name', type=str, help="specify name")


def run_cmd_choice(args) -> int:
    mirrors = get_mirrors(args)
    best = choice_mirror(mirrors, args.name)
    if best is not None:
        result = pipcli("config set global.index-url {best.url}".split())
        if result == 0:
            sys.stderr.write(f"choice {best.name}: {best.url}\n")
            sys.stdout.flush()
        return result
    return 0


def add_cmd(_arg: ArgSubParser):
    _arg.add_opt_on('-d', '--debug', help="show debug information")
    _arg.add_opt('-c',
                 '--config',
                 nargs=1,
                 type=str,
                 const=CONF_MIRRORS,
                 default=CONF_MIRRORS,
                 help="specify config file")
    _arg.add_subparsers(dest="sub_mirror")
    add_cmd_list(_arg.add_parser("list", help="list all mirrors"))
    add_cmd_get(_arg.add_parser("get", help="get mirror's url"))
    add_cmd_set(_arg.add_parser("set", help="set mirror's url"))
    add_cmd_now(_arg.add_parser("now", help="show config mirror"))
    add_cmd_choice(_arg.add_parser("choice", help="choice the best of mirror"))


def run_cmd(args) -> int:
    cmds = {
        "list": run_cmd_list,
        "get": run_cmd_get,
        "set": run_cmd_set,
        "now": run_cmd_now,
        "choice": run_cmd_choice,
    }
    if not hasattr(args, "sub_mirror"):
        return ENOENT
    args.mirrors = load(args.config)
    cmds[args.sub_mirror](args)


def main(argv: Optional[List[str]] = None) -> int:
    try:
        _arg = xarg("xpip-mirror",
                    description="pip mirror management",
                    epilog=f"For more, please visit {URL_PROG}")
        add_cmd(_arg)
        args = _arg.parse_args(argv)
        if args.debug:
            sys.stdout.write(f"{args}\n")
            sys.stdout.flush()
        return run_cmd(args)
    except KeyboardInterrupt:
        return ErrorCode.KeyboardInterrupt.value
    # except BaseException as e:
    #     sys.stderr.write(f"{e}\n")
    #     sys.stderr.flush()
    #     return ErrorCode.BaseException.value
