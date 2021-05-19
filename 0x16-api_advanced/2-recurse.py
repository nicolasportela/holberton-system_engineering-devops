#!/usr/bin/python3
""" Project 0x16. API advanced: Task 1 """
import requests


def recurse(subreddit, hot_list=[], next_page=""):
    """ Recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None."""

    headers = {'User-Agent': 'SoyYo!'}
    url = "https://www.reddit.com/r/" \
        + subreddit \
        + "/hot.json?after=" \
        + next_page
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        for element in res.json().get('data').get('children'):
            hot_list.append(element.get('data').get('title'))
        next_page = res.json().get('data').get('after')
        if next_page:
            recurse(subreddit, hot_list, next_page)
        return hot_list
    else:
        return None
    return hot_list
