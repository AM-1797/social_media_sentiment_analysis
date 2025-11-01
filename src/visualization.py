import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

def create_visualizations(df, brand):
    os.makedirs("visualizations", exist_ok=True)
    sns.countplot(data=df, x="sentiment", palette="Set2")
    plt.title(f"Sentiment Distribution for {brand}")
    plt.savefig(f"visualizations/{brand}_sentiment_distribution.png")
    plt.close()

    for sentiment in ["Positive", "Negative", "Neutral"]:
        text = " ".join(df[df["sentiment"] == sentiment]["cleaned_text"])
        if text:
            wc = WordCloud(width=800, height=400, background_color="white").generate(text)
            wc.to_file(f"visualizations/{brand}_{sentiment.lower()}_wordcloud.png")
