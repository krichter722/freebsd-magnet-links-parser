#!/usr/bin/python

# A script to parse magnet links from https://wiki.freebsd.org/Torrents and open
# them with the `deluge` GTK client.

import subprocess as sp
import plac

deluge_default = "deluge"

@plac.annotations(input_file_path=("The file which contains the magnet links (one per line)", "positional"),
    deluge=("The deluge binary to use", "option"),
)
def freebsd_magnet_link_parser(input_file_path, deluge=deluge_default):
    input_file = open(input_file_path, "r")
    input_file_lines = input_file.readlines()
    for input_file_line in input_file_lines:
        sp.check_call([deluge, input_file_line.strip()])

if __name__ == "__main__":
    plac.call(freebsd_magnet_link_parser)
