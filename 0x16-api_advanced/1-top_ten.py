#!/usr/bin/python3
"""queries Reddit API and prints titles of first 10 hot posts for subreddit"""

import requests


def top_ten(subreddit):
    """return 10 top posts"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}

    r = requests.get(url.format(subreddit),
                     allow_redirects=False,
                     headers=header)
    if r.status_code != 200:
        print (None)
    else:
        dic = r.json()
        for items in dic.get('data').get('children'):
            print (items['data']['title'])
