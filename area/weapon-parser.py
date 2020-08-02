#!/usr/bin/python3

import argparse
import linecache
import os
import re


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", dest="path",
                        help="specify an absolute path to area files, e.g. '/home/user/xania/area'")
    parser.add_argument("-type", "--type", dest="type",
                        help="specify a weapon type, e.g. 'sword'")
    parser.add_argument('--sort', dest='sort', action='store_true')
    parser.add_argument('--no-sort', dest='sort', action='store_false')
    parser.set_defaults(sort=True)
    options = parser.parse_args()

    if not options.type:
        parser.error(
            "Please specify a weapon type. Use --help for more information.")
    elif not options.path:
        parser.error(
            "Please specify a path to area files. Use --help for more information.")

    if options.type and os.path.exists(options.path):
        if any(".are" in file for file in os.listdir(options.path)):
            print("Area files found!")
            return options
        
    parser.error(
        "Please check your type and path. Use --help for more information.")

    
def find_weapons(type, path):
    print(f"Finding all {type}s in {path}.")
    pattern = re.compile(f"\B'{type}'\B \d \d")

    weapons = []

    for file in os.listdir(options.path):
        filename = options.path + "/" + file
        if os.path.splitext(filename)[1] == ".are":
            with open(filename) as area_file:
                for index, line in enumerate(area_file, 1):
                    if pattern.search(line):
                        # get the first string in the next line after a match
                        level = int(next(area_file, '').strip().split()[0])

                        # get a description 4 lines back. (this could be better)
                        description = linecache.getline(filename, index-4)

                        weapon = {
                            "area": filename.split('/')[-1],
                            "type": type,
                            "level": level,
                            "description": description
                        }
                        weapons.append(dict(weapon))
    return weapons
                    


options = get_arguments()

if options:
    weapons = find_weapons(options.type, options.path)
    
    if options.sort:
        weapons_sorted = sorted(weapons, key = lambda i: i['level'])
        for weapon in weapons_sorted:
            print(weapon)
    else:
        for weapon in weapons:
            print(weapon)

    