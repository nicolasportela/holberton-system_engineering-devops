#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], next_page=""):
    """returns titles of hot articles"""

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    url = "https://www.reddit.com/r/" \
        + subreddit \
        + "/hot.json?after=" \
        + next_page
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code != 200:
        return (None)
    else:
        dic = r.json()
        for item in dic.get('data').get('children'):
            hot_list.append(item.get('data').get('title'))
        next_page = dic.get('data').get('after')
        if next_page:
            recurse(subreddit, hot_list, next_page)
        return hot_list
