#projectlog.py

import sys

filepath = '/Users/Tadanori/dropbox/org/projectlog.txt'

if len(sys.argv) < 2:
    print(sys.argv[0])
    sys.exit()

with open(filepath) as f:
    l = f.readlines()

l.insert(0, sys.argv[1])

with open(filepath, mode='w') as f:
    f.writelines(l)