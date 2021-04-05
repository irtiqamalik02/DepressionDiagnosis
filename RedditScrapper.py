#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:23:26 2021

@author: irtiqamalik
"""

import praw
import csv
from datetime import datetime

# generate client_id,...,user_agent for using the PRAW API
reddit= praw.Reddit(client_id = '',
                    client_secret='',
                    username='',
                    password='',
                    user_agent='')
subreddit = reddit.subreddit("depression") # specify sub reddit as depression for depressed data
#subreddit = reddit.subreddit("AskReddit") # specify sub reddit as AskReddit for non-depressed data
hot_ask = subreddit.new(limit=1500000)
dict1 = {}

with open("dep_data.csv", "a", newline="") as file :
	fieldnames = ["id", "content", "date"]
	writer = csv.DictWriter(file, fieldnames=fieldnames)
	writer.writeheader()
	for post in hot_ask :
		writer.writerow({"id": str(post.id), "content": post.selftext, "date": datetime.fromtimestamp(post.created_utc).strftime("%Y-%m-%d %H:%M:%S")})
		post.comments.replace_more(limit=None)
		for comment in post.comments.list():
			writer.writerow({"id": str(comment.id), "content": comment.body, "date": datetime.fromtimestamp(comment.created_utc).strftime("%Y-%m-%d %H:%M:%S")})
