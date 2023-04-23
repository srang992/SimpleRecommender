"""
main streamlit app
"""
import pickle
import pandas as pd
import streamlit as st
from streamlit import session_state as session
from src.recommend.recommend import recommend_table


@st.cache_data(show_spinner=False)
def load_data():
    """
    load and cache data
    :return: tfidf data
    """
    tfidf_data = pd.read_feather("./data/tfidf_data.feather")
    tfidf_data = tfidf_data.set_index('title')
    return tfidf_data


tfidf = load_data()

with open("./data/movie_list.pickle", "rb") as f:
    movies = pickle.load(f)

dataframe = None

st.title("""
Netflix Recommendation System
This is a Content Based Recommender System made on implicit ratings :smile:.
 """)

st.text("")
st.text("")
st.text("")
st.text("")

session.options = st.multiselect(label="Select Movies", options=movies)

st.text("")
st.text("")

session.slider_count = st.slider(label="movie_count", min_value=5, max_value=50)

st.text("")
st.text("")

buffer1, col1, buffer2 = st.columns([1.45, 1, 1])

is_clicked = col1.button(label="Recommend")

if is_clicked:
    dataframe = recommend_table(session.options, movie_count=session.slider_count, tfidf_data=tfidf)

st.text("")
st.text("")
st.text("")
st.text("")

if dataframe is not None:
    st.table(dataframe)
