#!/usr/bin/env python3

import csv


class Yahoo:

    def __init__(self):
        print('inside __init__')
        self.uber_filename = 'UBER.csv'
        self.lyft_filename = 'LYFT.csv'

    def __enter__(self):
        print('inside __enter__')
        return self

    def __exit__(self,type_, value, traceback):
        print('inside __exit__')

if __name__ == '__main__':
    print('inside if name == main')
    print('outside Yahoo() 1')
    with Yahoo() as y:
        print('inside Yahoo()')
    print('outside Yahoo() 2')

