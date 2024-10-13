import streamlit as st
import pandas as pd

movies = pd.read_csv('data/movies.csv')
movies["year"] = movies['title'].str.extract(r"\((\d{4})\)$")

ratings = pd.read_csv('data/ratings.csv')

tags = pd.read_csv('data/tags.csv')

# Best rated movies

st.title("In case you don't know what to watch tonight...")

st.subheader(":red[Best rated movies]", divider="red")

st.write("""**Now if you want to choose a movie to watch tonight just take a look at the best rated movies.**""")

movies_ratings = movies.merge(ratings.groupby('movieId').mean(
).rename(columns={'rating': 'mean_rating'}), on='movieId')
movies_ratings_sorted = movies_ratings.sort_values(
    by='mean_rating', ascending=False)

st.write("Here are the 10 best rated movies")
for movie in movies_ratings_sorted.head(10).itertuples():
    st.markdown(f"{movie.title} : **{movie.mean_rating:.2f}** :star:")

st.subheader(":red[Best rated movies per genre]", divider="red")

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

st.subheader(":red[Best rated movies per year]", divider="red")

year = st.selectbox("Select a year", movies['year'].dropna().unique())
year_movies = movies[movies['year'] == year]
year_movies_ratings = year_movies.merge(ratings.groupby('movieId').mean(
).rename(columns={'rating': 'mean_rating'}), on='movieId')
year_movies_ratings_sorted = year_movies_ratings.sort_values(
    by='mean_rating', ascending=False)
st.write(f"Here are the 10 best rated movies from {year}")
for movie in year_movies_ratings_sorted.head(10).itertuples():
    st.markdown(f"{movie.title} : **{movie.mean_rating:.2f}** :star:")

st.subheader(":red[Number of ratings per movie]", divider="red")

movie = st.selectbox("Select a movie", movies['title'])
movie_ratings = ratings[ratings['movieId'] ==
                        movies[movies['title'] == movie].iloc[0]['movieId']]
ratings_per_movie = movie_ratings['rating'].value_counts().sort_index()
st.bar_chart(ratings_per_movie, color="#5555FF")