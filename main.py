import pandas as pd
import requests
import streamlit as st
import pickle


def recommend(movie):
    movies_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movies_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:6]
    recommended_movie=[]
    recommended_movie_posters=[]
    for i in movie_list:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movie.append(movies_list.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie, recommended_movie_posters


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=da307b36764882baac0290900d5912ff&language=en-US%27'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


st.title("Movie Recommender System")

movies_list=pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie = st.selectbox(
    'Choose a Movie',
    movies_list['title'].values)

if st.button('Recommend'):
    rec_names,rec_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(rec_posters[0])
        st.text(rec_names[0])

    with col2:
        st.image(rec_posters[1])
        st.text(rec_names[1])

    with col3:
        st.image(rec_posters[2])
        st.text(rec_names[2])

    with col4:
        st.image(rec_posters[3])
        st.text(rec_names[3])

    with col5:
        st.image(rec_posters[4])
        st.text(rec_names[4])