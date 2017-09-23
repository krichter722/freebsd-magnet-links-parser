#!/usr/bin/python

# A script to parse magnet links from https://wiki.freebsd.org/Torrents and open
# them with the `deluge` GTK client.

import subprocess as sp
import plac
import logging
import threading

logger = logging.getLogger('[name]')
deluge_default = "deluge"

@plac.annotations(input_file_path=("The file which contains the magnet links (one per line)", "positional"),
    deluge=("The deluge binary to use", "option"),
)
def freebsd_magnet_link_parser(input_file_path, deluge=deluge_default):
    input_file = open(input_file_path, "r")
    input_file_lines = input_file.readlines()
    #subprocess_threads = []
    for input_file_line in input_file_lines:
        if not input_file_line.startswith("magnet:"):
            logger.info("skipping line '%s'" % (input_file_line,))
            continue
        sp.check_call([deluge, input_file_line.strip()])
        # parallel adding doesn't work because deluge skips added torrents
        #def __deluge_call__():
        #    sp.check_call([deluge, input_file_line.strip()])
        #subprocess_thread = threading.Thread(target=__deluge_call__)
        #subprocess_thread.start()
        #subprocess_threads.append(subprocess_thread)
    #while len(subprocess_threads) > 0:
        #subprocess_threads[0].join()
        #subprocess_threads.remove(subprocess_threads[0])

if __name__ == "__main__":
    plac.call(freebsd_magnet_link_parser)
