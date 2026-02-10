import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt


st.title("IMDB Sentiment Analysis")


uploaded_file = st.file_uploader(
    "Upload IMDB Dataset CSV",
    type="csv"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    
    df['sentiment'] = df['sentiment'].map({
        'positive': 1,
        'negative': 0
    })

    st.write("Dataset Preview:")
    st.write(df.head())

    
    X_train, X_test, y_train, y_test = train_test_split(
        df['
