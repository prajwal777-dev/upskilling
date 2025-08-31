import streamlit as st
from textblob import TextBlob

st.title("Text Analyzer")
st.write("Paste any text below and analyze it")

user_input = st.text_area("Enter the text here: ")

if st.button("Analyze"):
    if user_input:
        no_of_words = len(user_input.split())
        no_of_chars = len(user_input)
        st.write("No of Words : ", no_of_words)
        st.write("No of Characters : ", no_of_chars)

        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        if polarity < 0:
            sentiment = "NEGATIVE"
        elif polarity > 0:
            sentiment = "POSITIVE"
        elif polarity == 0:
            sentiment = "NEUTRAL"
    
        st.write("Sentiment : ", sentiment)

    else:
        st.write("Please Enter Some Text to Analyze")
