#!/usr/bin/env python3

import csv


def csv_reader(file_path):
    with open(file_path, 'r') as f:
            rows = csv.reader(f)
            next(rows)
            for __ in rows:
                    print(__)

print('before name == main', __name__, '__main__')

if __name__ == '__main__':
    print('if name == main block', __name__, '__main__')
    csv_reader('LYFT.csv')
