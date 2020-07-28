#!/usr/bin/python

import argparse
import glob
import os
import re
import sys
import time
import traceback


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", dest="path",
                        help="specify an absolute path to log files, e.g. '/home/user/xania/logs'")
    options = parser.parse_args()

    if not options.path:
        parser.error(
            "Please specify a path. Use --help for more information.")

    if os.path.exists(options.path):
        if any(".log" in file for file in os.listdir(options.path)):
            print("Logs found.")
            return options

    parser.error(
        "Please specify a path with log files. Use --help for more information.")


def print_logs(interval):
    next_time = time.time() + interval

    while True:
        time.sleep(max(0, next_time - time.time()))
        try:
            print_recent_logins(options.path)
        except Exception:
            traceback.print_exc()
            # in production code you might want to have this instead of course:
            # logger.exception("Problem while executing repetitive task.")

        # skip tasks if we are behind schedule:
        next_time += (time.time() - next_time) // interval * \
            interval + interval


def print_recent_logins(text):
    print(os.listdir(options.path))
    for file in os.listdir(options.path):
        filename = options.path + "/" + file
        with open(filename) as myfile:
             for line in myfile:
                if "Successfully authorized" in line:
                    print(line)


options = get_arguments()

print_logs(5)
