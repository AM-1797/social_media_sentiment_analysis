import streamlit as st
import pandas as pd
from src.data_collection import fetch_tweets
from src.data_cleaning import clean_tweets
from src.sentiment_analysis import analyze_sentiments

st.title("🐦 Social Media Sentiment Analysis Dashboard")

brand = st.text_input("Enter brand name", "Zomato")

if st.button("Analyze"):
    with st.spinner("Fetching and analyzing tweets..."):
        df = fetch_tweets(brand, 100)
        df["cleaned_text"] = df["text"].apply(clean_tweets)
        df = analyze_sentiments(df)
        st.success("Analysis complete!")
        st.dataframe(df.head())
        st.bar_chart(df["sentiment"].value_counts())
