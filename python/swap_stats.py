#!/usr/bin/python

# an attempt to extract amount of swap used per process on linux machine

from __future__ import print_function

import re

smaps_file = '/Users/nkolchenko/playgarden/python/smaps'


def get_sums():
    sum_total = 0
    with open(smaps_file, 'r') as smaps_data:  # At the moment I'm on Mac thus parsing file copied from prod system
        for line in smaps_data.readlines():
            if "Swap" in line:
                line = re.sub('Swap:\D*', '', line)  # substitute "Swap: and all the non-digits symbols"
                # it is time to calculate kB , MB, etc. I assume  kB=1000Bytes
                line = re.sub(' kB', '000', line)
                line = re.sub(' MB', '000000', line)
                # print('Swap: '+str(line))
                line = int(line)
                sum_total = sum_total + line
        sum_total = sum_total / 1000
        sum_str = str(str(sum_total) + ' kB')
        # sum_str = str('Total Swap Usage: ' + str(sum_total) + ' kB')
    return sum_str


def main():
    print(get_sums())


def get_pids():
    # list of process ids in  /proc/ dir.
    return pids


def get_process_names():
    # process names for pids from get_pids()
    return names


if __name__ == '__main__':
    main()
