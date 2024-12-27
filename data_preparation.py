# import pandas as pd
# import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import os
# import pickle

# def create_data_directory():
#     """Create the data directory if it doesn't exist."""
#     os.makedirs('data', exist_ok=True)

# def load_and_preprocess_data():
#     """Load and preprocess the music dataset."""
#     # Load your music dataset
#     # Replace this with your actual data loading logic
#     # For example:
#     music_data = {
#         'song': [
#             'Shape of You', 'Blinding Lights', 'Dance Monkey', 'Sunflower',
#             'Someone You Loved', 'Stay', 'Levitating', 'Watermelon Sugar',
#             'Bad Guy', 'Perfect'
#         ],
#         'artist': [
#             'Ed Sheeran', 'The Weeknd', 'Tones and I', 'Post Malone',
#             'Lewis Capaldi', 'The Kid LAROI', 'Dua Lipa', 'Harry Styles',
#             'Billie Eilish', 'Ed Sheeran'
#         ],
#         'genre': [
#             'pop', 'synthpop', 'dance-pop', 'hip hop',
#             'pop', 'pop rap', 'disco', 'pop',
#             'electropop', 'pop'
#         ],
#         'year': [
#             2017, 2020, 2019, 2018,
#             2018, 2021, 2020, 2020,
#             2019, 2017
#         ]
#     }
    
#     music_df = pd.DataFrame(music_data)
#     return music_df

# def create_similarity_matrix(music_df):
#     """Create a similarity matrix based on song features."""
#     # Combine features for similarity calculation
#     features = music_df.apply(lambda x: ' '.join([
#         str(x['song']),
#         str(x['artist']),
#         str(x['genre']),
#         str(x['year'])
#     ]), axis=1)
    
#     # Create TF-IDF vectors
#     tfidf = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf.fit_transform(features)
    
#     # Calculate cosine similarity
#     similarity_matrix = cosine_similarity(tfidf_matrix)
#     return similarity_matrix

# def save_data(music_df, similarity_matrix):
#     """Save the processed data to pickle files."""
#     with open('data/music_list.pkl', 'wb') as f:
#         pickle.dump(music_df, f)
    
#     with open('data/similarity_matrix.pkl', 'wb') as f:
#         pickle.dump(similarity_matrix, f)

# def main():
#     """Main function to prepare the data."""
#     print("Starting data preparation...")
    
#     # Create data directory
#     create_data_directory()
#     print("Created data directory")
    
#     # Load and preprocess data
#     music_df = load_and_preprocess_data()
#     print(f"Loaded {len(music_df)} songs")
    
#     # Create similarity matrix
#     similarity_matrix = create_similarity_matrix(music_df)
#     print(f"Created similarity matrix of shape: {similarity_matrix.shape}")
    
#     # Save processed data
#     save_data(music_df, similarity_matrix)
#     print("Saved processed data to pickle files")
    
#     print("Data preparation complete!")

# if __name__ == "__main__":
#     main()
import pandas as pd

# Create a sample user history DataFrame (replace with real data if needed)
data = {
    'song': ['Song 1', 'Song 2', 'Song 3'],
    'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
    'timestamp': ['2024-12-27 14:00:00', '2024-12-27 14:05:00', '2024-12-27 14:10:00']
}

user_history_df = pd.DataFrame(data)

# Save it to a pickle file
user_history_df.to_pickle('user_history.pkl')

print("user_history.pkl file has been created successfully.")
