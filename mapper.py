#!/usr/bin/env python3

import sys

for line in sys.stdin:
    userid,itemid,rating = line.strip().split()[:3] # omiting timestamp5
    print(userid,itemid,rating)