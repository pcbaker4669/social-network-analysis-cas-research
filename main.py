import os
from dotenv import load_dotenv
import praw
import json
from datetime import datetime
from pathlib import Path

load_dotenv()

REDDIT_CONFIG = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "user_agent": os.getenv("REDDIT_USER_AGENT"),
    "username": os.getenv("REDDIT_USERNAME"),
    "password": os.getenv("REDDIT_PASSWORD"),
}


def save_posts(posts, subreddit, source):
    today = datetime.now()

    folder = Path(f"data/{today.year}/{today.month:02d}/{today.day:02d}")
    folder.mkdir(parents=True, exist_ok=True)

    filename = folder / f"{subreddit}_{source}.jsonl"

    with open(filename, "a", encoding="utf-8") as f:
        for post in posts:
            f.write(json.dumps(post) + "\n")

    print(f"Saved {len(posts)} posts to {filename}")

def get_fake_posts():
    return [
        {
            "id": "abc123",
            "title": "Test post 1",
            "score": 10,
            "created_utc": 1710000000
        },
        {
            "id": "def456",
            "title": "Test post 2",
            "score": 25,
            "created_utc": 1710001000
        }
    ]


def main():
    print("Reddit config loaded.")
    print(f"client_id present: {bool(REDDIT_CONFIG['client_id'])}")
    print(f"client_secret present: {bool(REDDIT_CONFIG['client_secret'])}")
    print(f"user_agent: {REDDIT_CONFIG['user_agent']}")
    print("Pipeline test running...")

    posts = get_fake_posts()
    save_posts(posts, "testsub", "new")


if __name__ == "__main__":
    main()