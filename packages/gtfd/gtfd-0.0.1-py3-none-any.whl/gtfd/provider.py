#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import subprocess
import string
import random
import json
import re
import time
import argparse
from pkg_resources import resource_string
from concurrent.futures import ThreadPoolExecutor, as_completed




ASCII_MODE = False

description = """TBomb - Your Friendly Spammer Application

TBomb can be used for many purposes which incudes -
\t Exposing the vulnerable APIs over Internet
\t Friendly Spamming
\t Testing Your Spam Detector and more ....

TBomb is not intented for malicious uses.
"""


def main():
    global ASCII_MODE, mesgdcrt
    parser = argparse.ArgumentParser(prog="gtfh",
                                     description=description,
                                     epilog='Coded by SpeedX !!!')
    parser.add_argument("-sms", "--sms", action="store_true",
                        help="start TBomb with SMS Bomb mode")
    parser.add_argument("-call", "--call", action="store_true",
                        help="start TBomb with CALL Bomb mode")
    parser.add_argument("-mail", "--mail", action="store_true",
                        help="start TBomb with MAIL Bomb mode")
    parser.add_argument("-ascii", "--ascii", action="store_true",
                        help="show only characters of standard ASCII set")
    parser.add_argument("-u", "--update", action="store_true",
                        help="update TBomb")
    parser.add_argument("-c", "--contributors", action="store_true",
                        help="show current TBomb contributors")
    parser.add_argument("-v", "--version", action="store_true",
                        help="show current TBomb version")
    args = parser.parse_args()
    if args.ascii:
        ASCII_MODE = True
        print("stat")
    if args.version:
        print("Version: ", "0.0.1")
    elif args.contributors:
        print("Contributors: ", "mr_gt")
    elif args.update:
        print("update")
    elif args.mail:
        print("main")
    elif args.call:
        print("call")
    elif args.sms:
        print("sms")
    else:
        print("hello 1")
    sys.exit()


if __name__ == "__main__":
    main()
