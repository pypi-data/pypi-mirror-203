#!/usr/bin/python3
# coding=utf-8

import sys
from errno import ENOENT
from typing import List, Optional

from xarg import ArgSubParser, xarg

from .xpip_config import URL_PROG
from .xpip_mirror import add_cmd as add_cmd_mirror
from .xpip_mirror import run_cmd as run_cmd_mirror
from .xpip_util import ErrorCode


def add_cmd(_arg: ArgSubParser):
    _arg.add_opt_on('-d', '--debug', help="show debug information")
    _arg.add_subparsers(dest="sub")
    add_cmd_mirror(_arg.add_parser("mirror"))


def run_command(args) -> int:
    cmds = {
        "mirror": run_cmd_mirror,
    }
    if not hasattr(args, "sub"):
        return ENOENT
    cmds[args.sub](args)


def main(argv: Optional[List[str]] = None) -> int:
    try:
        _arg = xarg("xpip",
                    description="Python package. Build. Install.",
                    epilog=f"For more, please visit {URL_PROG}")
        add_cmd(_arg)
        args = _arg.parse_args(argv)
        if args.debug:
            sys.stdout.write(f"{args}\n")
            sys.stdout.flush()
        return run_command(args)
    except KeyboardInterrupt:
        return ErrorCode.KeyboardInterrupt.value
    except BaseException as e:
        sys.stderr.write(f"{e}\n")
        sys.stderr.flush()
        return ErrorCode.BaseException.value
