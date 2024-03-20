#!/usr/bin/env python3

import math
import sys
import csv
from scipy.stats import pearsonr

def find_common_movies(user1, user2, userProfiles):
    """Find common movies rated by both user1 and user2."""
    movies_user1 = set(userProfiles.get(user1, {}).get("watched", {}).keys())
    movies_user2 = set(userProfiles.get(user2, {}).get("watched", {}).keys())
    common_movies = movies_user1.intersection(movies_user2)
    return common_movies

def extract_ratings(user, common_movies, userProfiles):
    """Extract ratings for common movies for a given user."""
    ratings = [userProfiles[user].get("watched", {}).get(movie, 0) for movie in common_movies]
    return ratings

def calculate_correlation(user1, user2, userProfiles):
    """Calculate Pearson correlation coefficient between two users based on their ratings."""
    common_movies = find_common_movies(user1, user2, userProfiles)
    if len(common_movies) < 2:
        return None 
    ratings_user1 = extract_ratings(user1, common_movies, userProfiles)
    ratings_user2 = extract_ratings(user2, common_movies, userProfiles)

    if len(set(ratings_user1)) == 1 or len(set(ratings_user2)) == 1:
        return None
    
    correlation, _ = pearsonr(ratings_user1, ratings_user2)
    return correlation

userProfiles = {}
for line in sys.stdin:
    user, movie, rating, timestamp = line.strip().split()
    rating = int(rating)
    if user not in userProfiles:
        userProfiles[user] = {"watched": {},"correlations": {}} 
    userProfiles[user]["watched"][movie] = rating 

for user, data in userProfiles.items():
    ratings = data["watched"].values()
    avg_rating = sum(ratings) / len(ratings) if ratings else 0 
    userProfiles[user]["avg_rating"] = avg_rating

users = list(userProfiles.keys())

for i in range(len(users)):
    for j in range(i+1,len(users)):
        correlation = calculate_correlation(users[i],users[j],userProfiles)
        if correlation is not None and not(math.isnan(correlation)== True):
            userProfiles[users[i]]["correlations"][users[j]] = userProfiles[users[j]]["correlations"][users[i]] = correlation
            print(f"{users[i]}, {users[j]} : {correlation}")

print(userProfiles)