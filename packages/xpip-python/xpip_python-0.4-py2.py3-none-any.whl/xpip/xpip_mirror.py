#!/usr/bin/python3
# coding=utf-8

import concurrent.futures
import sys
from urllib.parse import urlparse

from pip._internal.cli.main import main as pipcli
from tabulate import tabulate
from xarg import xarg, ArgSubParser

from .xpip_config import DIR_CONF, dump, load
from .xpip_util import connection_speed

CONF_MIRRORS = f"{DIR_CONF}/mirrors.toml"


def get_mirror(name: str, url: str) -> list:
    hostname = urlparse(url).hostname
    speed_ret = connection_speed(hostname)
    speed_val = speed_ret * 1000 if speed_ret is not None else -1.0
    return [name, url, hostname, speed_val]


def get_mirrors(args) -> "list[list]":
    mirrors = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for key in args.mirrors:
            mirror: dict = args.mirrors[key]
            url: str = mirror['url']
            futures.append(executor.submit(get_mirror, key, url))
        for future in concurrent.futures.as_completed(futures):
            mirrors.append(future.result())
    # sort by speed
    mirrors.sort(key=lambda x: x[3], reverse=False)
    # move "timeout" values to the end of the list
    mirrors = sorted(mirrors, key=lambda x: x[3] <= 0)
    for m in mirrors:
        m[3] = f"{m[3]:.01f}" if m[3] > 0 else "timeout"
    return mirrors


def choice_mirror(mirrors: "list[list]", name: str = None) -> list:
    if name is not None:
        for m in mirrors:
            if m[0] == name:
                return m
    elif len(mirrors) > 0 and mirrors[0][3] != "timeout":
        # choice the best of mirror
        return mirrors[0]

    return None


def add_cmd_list(_arg: ArgSubParser):
    pass


def run_cmd_list(args):
    mirrors = get_mirrors(args)
    # print table format
    table = tabulate(mirrors,
                     headers=['name', 'URL', 'HOST', 'PING'],
                     floatfmt='.1f')  # tablefmt='simple'
    sys.stderr.write(f"{table}\n")
    sys.stdout.flush()
    # choice the best of mirror
    best = choice_mirror(mirrors)
    if best is not None:
        sys.stderr.write("\nSuggest using the installation command:\n"
                         f"pip install -i {best[1]}\n")
    sys.stdout.flush()


def add_cmd_get(_arg: ArgSubParser):
    _arg.add_pos('name', type=str, nargs=1, help="specify name")


def run_cmd_get(args):
    _name = args.name
    if _name is not None and _name in args.mirrors:
        mirror: dict = args.mirrors[_name]
        sys.stderr.write(f"{mirror['url']}\n")
        sys.stdout.flush()


def add_cmd_set(_arg: ArgSubParser):
    _arg.add_pos('name', type=str, nargs=1, help="specify name")
    _arg.add_pos('url', type=str, nargs=1, help="specify url")


def run_cmd_set(args):
    _name = args.name
    _url = args.url
    if _name is not None and _url is not None:
        mirror = {_name: {'url': _url}}
        args.mirrors.update(mirror)
        dump(args.config, args.mirrors)


def add_cmd_now(_arg: ArgSubParser):
    pass


def run_cmd_now(args):
    pipcli(['config', 'get', 'global.index-url'])


def add_cmd_choice(_arg: ArgSubParser):
    _arg.add_pos('name', type=str, help="specify name")


def run_cmd_choice(args):
    mirrors = get_mirrors(args)
    best = choice_mirror(mirrors, args.name)
    if best is not None:
        name: str = best[0]
        url: str = best[1]
        result = pipcli(['config', 'set', 'global.index-url', url])
        if result == 0:
            sys.stderr.write(f"choice {name}: {url}\n")
            sys.stdout.flush()


def add_cmd(_arg: ArgSubParser):
    _arg.add_opt_on('-d', '--debug', help="show debug information")
    _arg.add_opt('-c',
                 '--config',
                 nargs=1,
                 type=str,
                 default=[CONF_MIRRORS],
                 help="specify config file")
    _arg.add_subparsers(dest="sub_mirror")
    add_cmd_list(_arg.add_parser("list", help="list all mirrors"))
    add_cmd_get(_arg.add_parser("get", help="get mirror's url"))
    add_cmd_set(_arg.add_parser("set", help="set mirror's url"))
    add_cmd_now(_arg.add_parser("now", help="show config mirror"))
    add_cmd_choice(_arg.add_parser("choice", help="choice the best of mirror"))


def run_cmd(args):
    _config = args.config[0]
    args.config = _config
    args.mirrors = load(args.config)
    {
        "list": run_cmd_list,
        "get": run_cmd_get,
        "set": run_cmd_set,
        "now": run_cmd_now,
        "choice": run_cmd_choice,
    }[args.sub_mirror](args)


def main():
    try:
        _arg = xarg("xpip-mirror", description="mirror")
        add_cmd(_arg)
        args = _arg.parse_args()
        if args.debug:
            sys.stdout.write(f"{args}\n")
            sys.stdout.flush()
        run_cmd(args)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.stderr.flush()
