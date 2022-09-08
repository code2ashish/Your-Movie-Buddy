import streamlit as st
import pickle
import pandas as pd
import requests

movie_list=pickle.load(open('Movies_dict.pkl','rb'))
movie_names=pd.DataFrame(movie_list)
similarity=pd.DataFrame(pickle.load(open("similarity.pkl",'rb')))

def fetch_poster(moive_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=ed0e787c5306207445c2ebda8a3addcf&language=en-US".format(moive_id))
    data=response.json()
    print()
    return "https://image.tmdb.org/t/p/original"+data['poster_path']


def recommand(movie):
    moive_index = movie_names[movie_names['title'] == movie].index[0]
    distance = similarity[moive_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    rec_movie=[]
    rec_movie_poster=[]
    for i in movie_list:
        movie_id=movie_names.iloc[i[0]].id
        rec_movie.append(movie_names.iloc[i[0]].title)
        rec_movie_poster.append(fetch_poster(movie_id))
    return rec_movie,rec_movie_poster

st.title('Movie Recommender For you❤')
option=st.selectbox("please select one",movie_names['title'].values)
if st.button("Recommand"):
    name,poster=recommand(option)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.header(name[0])
        st.image(poster[0])
    with col2:
        st.header(name[1])
        st.image(poster[1])
    with col3:
        st.header(name[2])
        st.image(poster[2])
    with col4:
        st.header(name[3])
        st.image(poster[3])
    with col5:
        st.header(name[4])
        st.image(poster[4])
