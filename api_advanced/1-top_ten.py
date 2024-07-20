#!/usr/bin/python3
"""
1-main
"""
import sys

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; top_ten/0.1; +http://example.com/bot)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status is not 200 (OK)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # If there are no posts, print None
        if not posts:
            print(None)
            return

        # Print the titles of the first 10 hot posts
        for post in posts[:10]:
            print(post.get('data', {}).get('title'))

    except requests.RequestException:
        print(None)
