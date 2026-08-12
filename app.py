import streamlit as st
import pandas as pd
import pickle

# Page Configuration
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# Custom CSS for aesthetic centering & cards
st.markdown("""
    <style>
    /* Main title styling */
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #888888;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }
    /* Section header */
    .section-header {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    /* Style recommendations display box */
    .rec-card {
        background-color: #1E1E24;
        border-radius: 8px;
        padding: 12px 16px;
        margin-bottom: 8px;
        border-left: 4px solid #FF4B4B;
        color: #FFFFFF;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# Cache resource loading for faster performance
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return pd.DataFrame(movies_dict), similarity

movies, similarity = load_data()

# Big Centered Title & Subtitle
st.markdown('<h1 class="main-title">🎬 Movie Recommendation System</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Discover your next favorite movie based on similarity algorithms</p>', unsafe_allow_html=True)

st.divider()

# Selection Area
st.markdown('<div class="section-header">Select a Movie You Like</div>', unsafe_allow_html=True)
selected_movie_name = st.selectbox(
    label='Movie Selection',
    options=movies['title'].values,
    label_visibility='collapsed'
)

# Recommendation Logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# Action Button & Output
st.write("")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    button_clicked = st.button('🚀 Get Recommendations', use_container_width=True, type="primary")

if button_clicked:
    st.write("")
    st.markdown('<div class="section-header">Recommended Movies</div>', unsafe_allow_html=True)
    st.write("")
    
    recommendations = recommend(selected_movie_name)
    for idx, movie_title in enumerate(recommendations, 1):
        st.markdown(f'<div class="rec-card">{idx}. {movie_title}</div>', unsafe_allow_html=True)