import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_tweets(keyword, limit=100):
    bearer_token = os.getenv("BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)
    query = f"{keyword} -is:retweet lang:en"
    tweets = client.search_recent_tweets(query=query, max_results=limit, tweet_fields=["created_at", "public_metrics"])

    data = []
    for tweet in tweets.data:
        data.append({
            "text": tweet.text,
            "created_at": tweet.created_at,
            "likes": tweet.public_metrics["like_count"],
            "retweets": tweet.public_metrics["retweet_count"]
        })

    return pd.DataFrame(data)
