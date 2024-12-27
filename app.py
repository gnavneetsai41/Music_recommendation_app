import os
import pickle
import spotipy
import streamlit as st
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id='0be1b8b5ddb449be8bbb3a8f2e82e796',
        client_secret='46a132213ca84fb69ab59404af83dbec'
    )
)


# Function to fetch album cover using Spotipy
def fetch_album_cover(song_name, artist_name):
    try:
        query = f"track:{song_name} artist:{artist_name}"
        results = spotify.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            return results['tracks']['items'][0]['album']['images'][0]['url']  # URL of album cover
        else:
            return "https://via.placeholder.com/150"  
    except Exception as e:
        print(f"Error fetching album cover: {e}")
        return "https://via.placeholder.com/150"  

def recommend(song):
    try:
        index = music[music['song'] == song].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        
        recommended_song_names = []
        recommended_album_covers = []
        recommended_artists = []
        
        for i in distances[1:6]: 
            song_name = music.iloc[i[0]].song
            artist_name = music.iloc[i[0]].artist
            
            # Fetch album cover for each recommendation
            recommended_album_covers.append(fetch_album_cover(song_name, artist_name))
            recommended_song_names.append(song_name)
            recommended_artists.append(artist_name)
        
        return recommended_song_names, recommended_album_covers, recommended_artists
    except Exception as e:
        print(f"Error in recommendation function: {e}")
        return [], [], []

try:
    music = pd.read_pickle('music_list (2).pkl')  
    with open('similarity (2).pkl', 'rb') as f:
        similarity = pickle.load(f) 
except FileNotFoundError as e:
    print(f"Error loading files: {e}")
    st.error("Required files are missing. Please check your file paths.")
    music, similarity = None, None

st.header('Music Recommender System 🎵')

if music is not None:
    song_list = music['song'].values
    selected_song = st.selectbox(
        "Type or select a song from the dropdown",
        song_list
    )

    if st.button('Show Recommendation'):
        try:
            recommended_song_names, recommended_album_covers, recommended_artists = recommend(selected_song)
            
            if recommended_song_names:
                cols = st.columns(len(recommended_song_names)) 
                for idx, col in enumerate(cols):
                    with col:
                        st.text(recommended_song_names[idx])
                        st.text(recommended_artists[idx])
                        st.image(recommended_album_covers[idx])
            else:
                st.warning("No recommendations found. Please try another song.")
        except Exception as e:
            st.error(f"Error generating recommendations: {e}")
else:
    st.warning("Music data could not be loaded. Please ensure all required files are in place.")
