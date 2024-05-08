#!/usr/bin/python3
""" prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """prints the top10"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')
        [print(post.get('data').get('title')) for post in posts]
    else:
        print(None)
