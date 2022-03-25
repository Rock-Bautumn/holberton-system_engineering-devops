#!/usr/bin/python3
"""testing file"""


import csv

with open('names.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, dialect=csv.unix_dialect)
    writer.writeheader()
    # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
