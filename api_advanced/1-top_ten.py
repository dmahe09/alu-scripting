
import requests

def top_ten(subreddit
    reddit_url = "https/www.reddit.com/r/{}/hot.json" \
        .format(subreddit
    headers = headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)
    if response.status_code == 200:
        data = 
        import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
        print(None)
        return

    for post in posts[:10]:
        print(post.get('data', {}).get('title'))
