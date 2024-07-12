import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Load the dataset
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Create a user-item matrix
user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Convert the user-item matrix to a sparse matrix
user_item_matrix_sparse = csr_matrix(user_item_matrix.values)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix_sparse)

def get_movie_recommendations(user_id, user_similarity, user_item_matrix, movies, n_recommendations=5):
    # Adjust for 1-based index
    user_index = user_id - 1
    
    # Get similarity scores for the given user
    similar_users = user_similarity[user_index]
    
    # Calculate weighted sum of ratings from similar users
    weighted_sum = user_item_matrix.values.T.dot(similar_users)
    
    # Convert to a Series for easier manipulation
    weighted_sum = pd.Series(weighted_sum, index=user_item_matrix.columns)
    
    # Sort the weighted sum in descending order
    weighted_sum = weighted_sum.sort_values(ascending=False)
    
    # Identify movies the user has already watched
    watched_movies = user_item_matrix.columns[user_item_matrix.iloc[user_index] > 0]
    
    # Drop watched movies from the recommendation list
    recommendations = weighted_sum.drop(watched_movies).head(n_recommendations).index
    
    # Get the movie titles for the recommended movies
    recommended_movies = movies[movies['movieId'].isin(recommendations)]
    
    return recommended_movies['title'].values

# Example usage
user_id = 1
recommended_movies = get_movie_recommendations(user_id, user_similarity, user_item_matrix, movies)
print("Recommended Movies:", recommended_movies)
