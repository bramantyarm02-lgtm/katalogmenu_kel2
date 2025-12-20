#!/usr/bin/env python3

import sys


s = 0
for data in sys.stdin:
    s += float(data)

print(s)
