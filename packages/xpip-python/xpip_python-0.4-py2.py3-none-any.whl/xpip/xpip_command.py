#!/usr/bin/python3
# coding=utf-8

import sys

from xarg import xarg

from .xpip_config import URL_PROG
from .xpip_mirror import add_cmd as add_cmd_mirror
from .xpip_mirror import run_cmd as run_cmd_mirror


def run_sub_command(args):
    {
        "mirror": run_cmd_mirror,
    }[args.sub](args)


def main():
    try:
        _arg = xarg("xpip",
                    description="Python package. Build. Install.",
                    epilog=f"For more, please visit {URL_PROG}")
        _arg.add_opt_on('-d', '--debug', help="show debug information")
        _arg.add_subparsers(dest="sub")
        add_cmd_mirror(_arg.add_parser("mirror"))
        args = _arg.parse_args()
        if args.debug:
            sys.stdout.write(f"{args}\n")
            sys.stdout.flush()
        run_sub_command(args)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.stderr.flush()
