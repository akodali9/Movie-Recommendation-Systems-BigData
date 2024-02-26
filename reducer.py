#!/usr/bin/env python3

import sys

output = dict()
output_movie = dict()

for line in sys.stdin:

    userid,itemid,rating= line.strip().split()
    if userid in output.keys():
        output[userid]['rating'] += int(rating)
        output[userid]['count'] += 1
    else:
        output[userid] = dict()
        output[userid]['rating']= int(rating)
        output[userid]['count'] = 1

    if itemid in output_movie.keys():
        output_movie[itemid]['rating'] += int(rating)
        output_movie[itemid]['count'] += 1
    else:
        output_movie[itemid] = dict()
        output_movie[itemid]['rating']= int(rating)
        output_movie[itemid]['count'] = 1
print("user\tcount\taverage rating")
for user in output.keys():
    average_rating_user = round(float(output[user]['rating'])/output[user]['count'])
    if(average_rating_user>=5):
        print(f"{user}\t{output[user]['count']}\t{average_rating_user}")
print("\n\n")
print("movie\tcount\taverage rating")
for movie in output_movie.keys():
    average_rating_movie = round(float(output_movie[movie]['rating'])/output_movie[movie]['count'])
    if(output_movie[movie]['count']>=10 and average_rating_movie>=4):
        print(f"{movie}\t{output_movie[movie]['count']}\t{average_rating_movie}")