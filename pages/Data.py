import streamlit as st
import pandas as pd
import altair as alt

st.title('Data Visualization')

st.subheader("The movies dataset")
movies = pd.read_csv('data/movies.csv')

movies["year"] = movies['title'].str.extract(r"\((\d{4})\)$")
st.dataframe(movies.head())

st.subheader("Number of movies per year")
movies_per_year = movies['year'].value_counts().sort_index()
st.bar_chart(movies_per_year, color="#FF5555")

st.subheader("The ratings dataset")
ratings = pd.read_csv('data/ratings.csv')
st.dataframe(ratings.head())

st.subheader("The tags dataset")
tags = pd.read_csv('data/tags.csv')
st.dataframe(tags.head())

st.divider()

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

ratings["dates"] = pd.to_datetime(ratings['timestamp'], unit='s')
ratings['year'] = ratings['dates'].dt.year
ratings['month'] = ratings['dates'].dt.month

st.subheader("Number of ratings per year")
ratings_per_year = ratings['year'].value_counts().sort_index()
st.bar_chart(ratings_per_year, color="#00CC00")

months = st.tabs(["January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"])

months_str = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

months_color = ["#FF5555", "#FFAA00", "#FFFF00", "#AAFF00", "#55FF00", "#00FF00",
                "#00FF55", "#00FFAA", "#00FFFF", "#00AAFF", "#0055FF", "#0000FF"]

for month in months:
    with month:
        st.subheader(f"Number of ratings in {months_str[months.index(month)]}")
        ratings_per_month = ratings[ratings['month'] == months.index(
            month) + 1]['year'].value_counts().sort_index()
        st.bar_chart(ratings_per_month, color=months_color[months.index(month)])

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

st.subheader("Best rated movies")

movies_ratings = movies.merge(ratings.groupby('movieId').mean(
).rename(columns={'rating': 'mean_rating'}), on='movieId')
movies_ratings_sorted = movies_ratings.sort_values(by='mean_rating', ascending=False)

st.write("Here are the 10 best rated movies")
for movie in movies_ratings_sorted.head(10).itertuples():
    st.markdown(f"{movie.title} : **{movie.mean_rating:.2f}** :star:")


st.subheader("Best rated movies per genre")

genre = st.selectbox("Select a genre", movies['genres'].str.split(
    '|', expand=True).stack().unique())
genre_movies = movies[movies['genres'].str.contains(genre)]
genre_movies_ratings = genre_movies.merge(ratings.groupby('movieId').mean(
).rename(columns={'rating': 'mean_rating'}), on='movieId')
genre_movies_ratings_sorted = genre_movies_ratings.sort_values(
    by='mean_rating', ascending=False)
st.write(f"Here are the 10 best rated {genre} movies")
for movie in genre_movies_ratings_sorted.head(10).itertuples():
    st.markdown(f"{movie.title} : **{movie.mean_rating:.2f}** :star:")