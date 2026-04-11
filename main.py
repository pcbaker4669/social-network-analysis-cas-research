import os
from dotenv import load_dotenv

load_dotenv()

REDDIT_CONFIG = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "user_agent": os.getenv("REDDIT_USER_AGENT"),
    "username": os.getenv("REDDIT_USERNAME"),
    "password": os.getenv("REDDIT_PASSWORD"),
}


def main():
    print("Reddit config loaded.")
    print(f"client_id present: {bool(REDDIT_CONFIG['client_id'])}")
    print(f"client_secret present: {bool(REDDIT_CONFIG['client_secret'])}")
    print(f"user_agent: {REDDIT_CONFIG['user_agent']}")


if __name__ == "__main__":
    main()