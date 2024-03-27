#!/usr/bin/env python3

import json
import sys

data = {}
movie_list = []

def load_json(line):
    try:
        data = json.loads(line)
        return data
    except json.JSONDecodeError as e:
        sys.stderr.write(f"{e}")

def findNotWatched(user):
    return list(set(data[user]["watched"].keys()).symmetric_difference(set(movie_list)))

def findreviewers(movie):
    reviewers = []
    for user,data_item in data.items():
        if movie in data_item["watched"].keys():
            reviewers.append({"reviewer":user,"rating":data_item["watched"][movie]})
    return reviewers

def findCorrelation(user1,user2):
    if data.get(user1) and data[user1].get("correlations") and data[user1]["correlations"].get(user2):
        return data[user1]["correlations"][user2]
    return 0


def predictRating(user,reviewers):
    sum_correlation = 0
    total_value = 0
    for reviewer in reviewers:
        correlation = findCorrelation(user,reviewer["reviewer"])
        total_value +=reviewer["rating"]*correlation
        sum_correlation +=correlation
    if sum_correlation > 0:
        return total_value/sum_correlation
    return 0

def getmovies():
    for value in data.values():
        for i in value["watched"].keys():
            if i not in movie_list:
                movie_list.append(i)

if __name__ == "__main__":
    for line in sys.stdin:
        data = load_json(line.strip())
    getmovies()
    for user in data.keys():
        print(user)
        notWatched = findNotWatched(user)
        data[user]["not_watched_prediction"] = dict()
        for movie_not_watched in notWatched:
            reviewers = findreviewers(movie_not_watched)
            print(reviewers)
            predicted_rating = predictRating(user,reviewers)
            data[user]["not_watched_prediction"][movie_not_watched] = predicted_rating
    with open("./json_output_file.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(json.dumps(data,indent=4))