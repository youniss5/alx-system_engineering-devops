#!/usr/bin/python3
"""
Script that queries API & returns the numb of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """ Returns number of subscribers """
    if subreddit is None or type(subreddit) is not str:
        return (0)

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {'User-Agent': 'my-app'}
    response = requests.get(url, headers=head, allow_redirects=False)

    try:
        return (response.json().get("data").get("subscribers"))
    except Exception:
        return (0)
