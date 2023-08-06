#!/usr/bin/python3

import argparse
import concurrent.futures
import math
import sys
from datetime import datetime
import hashlib
import os.path
from threading import Lock

LOCK = Lock()

RUN = True
ARGS = None
COUNT = 0

PASSWORDS = []

FOUND = []
def print_safe(string):
    with LOCK:
        print(string)


def show_version():
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, './VERSION')) as version_file:
        version = version_file.read().strip()
        print("v" + version)


def show_header():
    # Need to add a header here
    show_version()

    print('https://gitlab.cylab.be/cylab/whitechapel')
    print('Use for legal purposes only!')
    print('')


# Function to compute MD5 hash
def compute_md5_hash(string):
    '''
    Compute the MD5 hash of a string
    :param string:
    :return:
    '''
    string = string.strip()
    hash = hashlib.md5(string.encode()).hexdigest()
    print_safe("Password: " + string + " - Hash: " + hash)
    if ARGS.hash == hash:
        FOUND.append(string)
        print_safe("FOUND PASSWORD: " + string + " - Hash: " + hash + "")
        if ARGS.stop_on_first:
            global RUN
            RUN = False


def compute_hashes(hashes):
    '''
    Compute a list of hashes
    :param hash:
    :return:
    '''
    for hash in hashes:
        global COUNT
        COUNT += 1
        if not RUN:
            break
        compute_md5_hash(hash)



def islice(iterable, *args):
    '''
    https://docs.python.org/3/library/itertools.html#recipes
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    '''
    slices = slice(*args)
    start, stop, step = slices.start or 0, slices.stop or sys.maxsize, slices.step or 1
    iterations = iter(range(start, stop, step))
    try:
        nexti = next(iterations)
    except StopIteration:
        # Consume *iterable* up to the *start* position.
        for i, element in zip(range(start), iterable):
            pass
        return
    try:
        for i, element in enumerate(iterable):
            if i == nexti:
                yield element
                nexti = next(iterations)
    except StopIteration:
        # Consume to *stop*.
        for i, element in zip(range(i + 1, stop), iterable):
            pass

def batched(iterable, count):
    '''
    Batch data into tuples of length count. The last batch may be shorter.
    https://docs.python.org/3/library/itertools.html#recipes

    >>> list(batched('ABCDEFG', 3))
    [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
    '''
    if count < 1:
        raise ValueError('n must be at least one')
    iterable = iter(iterable)
    while (batch := tuple(islice(iterable, count))):
        yield batch

def parse_args():
    '''
    Parse command line arguments
    :return:
    '''
    global ARGS
    parser = argparse.ArgumentParser(description='Whitechapel')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-p', '--passwords', help='Passwords file', required=True)
    parser.add_argument('-t', '--threads', help='Number of threads', default=1, type=int)
    # parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument('-s', '--hash', help='Hash', required=True)
    parser.add_argument('--stop-on-first', help='Stop on first match', action='store_true')

    ARGS = parser.parse_args()


def validate_args():
    '''
    Validate command line arguments
    :return:
    '''
    if not os.path.isfile(ARGS.passwords):
        print("Passwords file does not exist")
        exit(1)
    # Check if a string has the structure for a MD5 hash
    if not ARGS.hash.isalnum() or len(ARGS.hash) != 32:
        print("Hash is not a valid MD5 hash")
        exit(1)

def read_passwords():
    '''
    Read passwords from a file
    :return:
    '''
    global PASSWORDS
    with open(ARGS.passwords, "r") as passwords_file:
        PASSWORDS = passwords_file.readlines()


def run():

    passwords_per_thread = math.ceil(float(len(PASSWORDS)) / ARGS.threads)
    print("Hash: " + ARGS.hash)
    print("Threads: " + str(ARGS.threads))
    print("Passwords: " + str(len(PASSWORDS)))
    print("Passwords per thread: " + str(passwords_per_thread))

    # https://stackoverflow.com/a/15143994
    executor = concurrent.futures.ThreadPoolExecutor(ARGS.threads)
    futures = [executor.submit(compute_hashes, group)
        for group in batched(PASSWORDS, passwords_per_thread)]

    # https://stackoverflow.com/a/65207578
    try:
        concurrent.futures.wait(futures)
    except KeyboardInterrupt:
        # User interrupt the program with ctrl+c
        print_safe("Stopping threads...")
        global RUN
        RUN = False
        executor.shutdown(wait=True, cancel_futures=True)
        sys.exit()
def main():
    '''
    Main function
    :return:
    '''
    start = datetime.now()
    show_header()
    parse_args()
    validate_args()
    read_passwords()

    run()

    print("Done!")
    end = datetime.now()
    delta_t = (end - start).total_seconds()
    rate = COUNT /delta_t
    print("Time: " + str(delta_t) + " seconds [" + str(round(rate, 2)) + " passwords/sec]")
    print("Found " + str(len(FOUND)) + " password(s): " + str(FOUND))


if __name__ == '__main__':
    main()