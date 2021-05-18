#!/usr/bin/python3
"""queries Reddit API and returns number of subscribers for given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """return number of subscribers"""

    url = 'https://www.reddit.com/r/{}/about.json'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}

    r = requests.get(url.format(subreddit),
                     allow_redirects=False,
                     headers=header)
    if r is False:
        return 0
    else:
        return (r.get('data[subscribers]'))
