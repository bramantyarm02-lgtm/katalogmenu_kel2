#!/usr/bin/env python3

import sys
import json


data = json.loads(sys.stdin.read())
print(sum(data))
