from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import pandas as pd

nltk.download("vader_lexicon", quiet=True)

def analyze_sentiments(df):
    analyzer = SentimentIntensityAnalyzer()
    results = []
    for text in df["cleaned_text"]:
        score = analyzer.polarity_scores(text)
        polarity = TextBlob(text).sentiment.polarity
        if score["compound"] > 0.05:
            sentiment = "Positive"
        elif score["compound"] < -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        results.append({
            "compound": score["compound"],
            "polarity": polarity,
            "sentiment": sentiment
        })
    return pd.concat([df, pd.DataFrame(results)], axis=1)
