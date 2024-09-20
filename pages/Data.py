import streamlit as st
import pandas as pd
import altair as alt

st.title('Data Visualization')

movies = pd.read_csv('data/movies.csv')

st.subheader("The movies dataset")
st.dataframe(movies.head())

ratings = pd.read_csv('data/ratings.csv')

st.subheader("The ratings dataset")
st.dataframe(ratings.head())

st.subheader("Number of movies per genre")
genres = movies['genres'].str.split('|', expand=True).stack().value_counts().sort_values(ascending=False)

# Same chart with altair and one color per bar

genres = genres.reset_index()
genres.columns = ['genre', 'count']
genres_chart = alt.Chart(genres).mark_bar().encode(
    x='count',
    y=alt.Y('genre', sort='-x'),
    color='genre'
)
st.altair_chart(genres_chart, use_container_width=True)

ratings ["dates"] = pd.to_datetime(ratings['timestamp'], unit='s')
ratings['year'] = ratings['dates'].dt.year
ratings['month'] = ratings['dates'].dt.month

st.subheader("Number of ratings per year")
ratings_per_year = ratings['year'].value_counts().sort_index()
st.line_chart(ratings_per_year, color="#00CC00")

months = st.tabs(["January", "February", "March", "April", "May", "June", "July", 
"August", "September", "October", "November", "December"])

months_str = ["January", "February", "March", "April", "May", "June", "July",
"August", "September", "October", "November", "December"]

for month in months:
    with month:
        st.subheader(f"Number of ratings in {months_str[months.index(month)]}")
        ratings_per_month = ratings[ratings['month'] == months.index(month) + 1]['year'].value_counts().sort_index()
        st.line_chart(ratings_per_month, color="#FF5555")

tags = pd.read_csv('data/tags.csv')

st.subheader("Number of movies per tag")

st.dataframe(tags.head())

st.markdown(f"There is **{len(tags['tag'].unique())}** unique tags")
st.write("Here are the **30** most used tags")


fig = alt.Chart(tags['tag'].value_counts().head(30).reset_index()).mark_bar().encode(
    x='count',
    y=alt.Y('tag', sort='-x'),
    color='tag'
)
st.altair_chart(fig, use_container_width=True)

links = pd.read_csv('data/links.csv')

st.subheader("The links dataset")
st.dataframe(links.head())

st.subheader("Number imdbId/tmdbId per movieId")
