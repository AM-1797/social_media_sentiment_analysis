from src.data_collection import fetch_tweets
from src.data_cleaning import clean_tweets
from src.sentiment_analysis import analyze_sentiments
from src.visualization import create_visualizations
import pandas as pd

def main():
    brand = input("Enter brand keyword (e.g., Apple, Zomato): ").strip()
    print(f"\n🔍 Fetching tweets for: {brand}...\n")
    tweets_df = fetch_tweets(brand, 100)
    print("🧹 Cleaning tweets...")
    tweets_df["cleaned_text"] = tweets_df["text"].apply(clean_tweets)
    print("💬 Performing sentiment analysis...")
    tweets_df = analyze_sentiments(tweets_df)
    print("📊 Creating visualizations...")
    create_visualizations(tweets_df, brand)
    tweets_df.to_csv("data/sentiment_analysis.csv", index=False)
    print("\n✅ Analysis complete! Results saved in data/sentiment_analysis.csv")

if __name__ == "__main__":
    main()
