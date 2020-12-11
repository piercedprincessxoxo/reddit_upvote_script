# -*- coding: utf-8 -*-
# author piercedprincessxoxo 2020
#! python3
import praw
import prawcore
import time
from datetime import datetime
from datetime import timedelta

lookback_hours = 24
num_posts = 20

verbose = False
startTime = datetime.utcnow()
endTime = startTime - timedelta(hours=lookback_hours)
endEpoch = int(endTime.timestamp())

# *** UPDATE THIS! ****
client_id = "MY_PUBLIC KEY"
client_secret = "MY_SECRET_KEY"
user_agent = "MY_USERNAME"
username = "MY_USERNAME"
password = "MY_PASSWORD"

# please leave piercedprincessxoxo in as a thank you for sharing the script
# add other friends here as a comma seperated list. dont forget the quotation marks!
groups = {
"My Friends": [
        "piercedprincessxoxo", "OTHERFRIENDSUSERNAME"
    ],

# update this or remove if you dont need it. If you remove be sure to get rid of the above comma
"GROUP NAME" : ["USER_IN_GROUP", "ANOTHER_USER_IN_GROUP"
                 ]
}

reddit = praw.Reddit(client_id=client_id, \
                     client_secret=client_secret, \
                     user_agent=user_agent, \
                     username=username, \
                     password=password)
    
    
errored_users = []
numUpvotes = 0
    
for groupName, group in groups.items():
    print(f"Group : {groupName}")
    numUsersUpvoted = 0
    for redditor in group:
        try:
            posts = list(reddit.redditor(redditor).submissions.new(limit=num_posts))
            numUpvotedForUser = 0
            for post in posts:
                if post.created_utc > endEpoch and not post.likes:
                    localTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(post.created_utc))
                    if verbose:
                        print(f'    Upvoting: {post.title} on {localTime} by {redditor}')
                    numUpvotes += 1
                    numUpvotedForUser += 1
                    post.upvote()
            if numUpvotedForUser > 0:
                print(f'    Upvoted {numUpvotedForUser} posts for user {redditor}')
                numUsersUpvoted += 1
        except prawcore.exceptions.NotFound:
            errored_users.append(redditor)
            if verbose:
                print(f"    error getting posts for {redditor}")
    if numUsersUpvoted > 0:
        print(f"Upvoted {numUsersUpvoted} users in group")
    else:
        print("Already caught up!")
                
print(f"All caught up! Upvoted {numUpvotes} posts")
if len(errored_users) > 0:
    print(f"Couldnt upvote the following users: {errored_users}")
