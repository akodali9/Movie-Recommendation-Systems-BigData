#!/usr/bin/env python3

import sys
userprofiles = {}
for line in sys.stdin:
    userid,itemid,rating = line.strip().split()[:3] # omiting timestamp5
    rating = int(rating)
    if userid in userprofiles.keys():
        userprofiles[userid]["watched"].append({itemid:rating})
    else:
        userprofiles[userid] = dict()
        userprofiles[userid]["watched"] = list()
        userprofiles[userid]["watched"].append({itemid:rating})
for userid,data in userprofiles.items():

    total_sum = sum(sum(dictionary.values()) for dictionary in data["watched"])
    total_len = len([sum(dictionary.values()) for dictionary in data["watched"]])
    userprofiles[userid]["avg_rating"] = total_sum/total_len

for userid,data in userprofiles.items():
    print("{"+f"{userid}:{data}"+"}")