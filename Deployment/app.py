import requests
import pickle
import pandas as pd
import streamlit as st


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=258772fb163aa88d210621a41326ef67'
                            .format(movie_id))
    data = response.json()
    backdrop_p = data['backdrop_path']
    poster_p = data['poster_path']

    return 'https://image.tmdb.org/t/p/w500/' + backdrop_p, 'https://image.tmdb.org/t/p/w500/' + poster_p


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # To get index of corresponding movie
    distance = similarity[movie_index]
    movielist = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    # Sorting in descending order to get movies with best match
    recommended_movies = []
    recommended_movies_poster = []
    for a in movielist:
        recommended_movies.append(movies.iloc[a[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[a[0]].movie_id))

    return recommended_movies, recommended_movies_poster


st.title('Movie Recommendation System')

movie_st = pickle.load(open('new_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_st)
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    'Please select a Movie',
    movies['title'].values
    # Here, tuple is preferred because it will have immutable values and hence can't be changed by anyone
)

if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)

    for i in range(0, 5):
        st.title('Recommendation {}'.format(i+1))
        st.header('Name:')
        st.text(names[i])

        col1, col2 = st.columns(2)

        with col1:
            st.header('Backdrop:')
            st.image(poster[i][0])

        with col2:
            st.header('Main Poster:')
            st.image(poster[i][1])
