# check_format.py
from sys import argv
import csv
import os

from qiime2.plugin import ValidationError

filepath = os.path.join(argv[1])

def check_header(header_line: list):
    if header_line != ['utensil', 'action', 'materials', 'bagel']:
        raise ValidationError("No header present or header does not contain"
                " correct fields")

with open(filepath) as fh:
    for i, line in enumerate(fh, 0):
        if i == 0:
            check_header([field.rstrip() for field in line.split(sep='\t')])
        print(line)
