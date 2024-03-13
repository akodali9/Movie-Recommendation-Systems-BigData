#!/usr/bin/env python3

import json
import sys

user_rating = dict()
movie_rating = dict()

def recommend(user_rating,movie_rating):
    recommendation = dict()
    for userid,data in user_rating.items():
        avg = sum(data['ratings'])/len(data['ratings'])
        recommendation[userid] = {'avg_rating': avg,'watched':data['movies'],'recommend':[]}
    for movieid,movierating in movie_rating.items():
        mov_avg = sum(movierating)/len(movierating)
        for userid,userdata in recommendation.items():
            if(abs(userdata['avg_rating']-mov_avg)<=0.5 and movieid not in userdata['watched']):
                recommendation[userid]['recommend'].append({movieid : userdata['avg_rating']-mov_avg})
            
    for userid,userdata in recommendation.items():
        sorted_recommend = sorted(recommendation[userid]["recommend"], key=lambda x: list(x.values())[0],reverse=True)
        recommendation[userid]["recommend"] = sorted_recommend
    for userid,userdata in recommendation.items():
        print(f'{userid}\tshould watch movies with id as\t{recommendation[userid]["recommend"][:5]}')
    formatted_json = json.dumps(recommendation, indent=4)
    # print(formatted_json)
for line in sys.stdin:
    userid,itemid,rating= line.strip().split()
    rating = int(rating)
    if userid in user_rating.keys():
        user_rating[userid]['ratings'].append(int(rating))
        if itemid not in user_rating[userid]['movies']:
            user_rating[userid]['movies'].append(itemid)
    else:

        user_rating[userid] = dict()
        user_rating[userid]['ratings'] = list()
        user_rating[userid]['ratings'].append(int(rating))
        user_rating[userid]['movies'] = list()
        user_rating[userid]['movies'].append(itemid)

    if itemid in movie_rating.keys():
        movie_rating[itemid].append(int(rating))
    else:
        movie_rating[itemid] = list()
        movie_rating[itemid].append(int(rating))

recommend(user_rating,movie_rating)