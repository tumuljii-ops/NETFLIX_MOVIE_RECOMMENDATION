import pickle
import pandas as pd

# ==========================================
# LOAD MODEL
# ==========================================

with open("nmf_model.pkl", "rb") as f:
    model = pickle.load(f)

# ==========================================
# LOAD RATINGS
# ==========================================

ratings_cols = [
    "user_id",
    "movie_id",
    "rating",
    "timestamp"
]

ratings_df = pd.read_csv(
    "ml-100k/ml-100k/u.data",
    sep="\t",
    names=ratings_cols
)

# ==========================================
# LOAD MOVIES
# ==========================================

movie_cols = [
    "movie_id",
    "title",
    "release_date",
    "video_release_date",
    "IMDb_URL",
    "unknown",
    "Action",
    "Adventure",
    "Animation",
    "Children",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Fantasy",
    "Film-Noir",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "War",
    "Western"
]

movies_df = pd.read_csv(
    "ml-100k/ml-100k/u.item",
    sep="|",
    encoding="latin-1",
    names=movie_cols
)

# ==========================================
# TOP RECOMMENDATIONS
# ==========================================

def get_top_recommendations(user_id, top_n=5):

    watched_movies = set(
        ratings_df[
            ratings_df["user_id"] == user_id
        ]["movie_id"]
    )

    recommendations = []

    for movie_id in movies_df["movie_id"]:

        if movie_id in watched_movies:
            continue

        pred = model.predict(
            uid=user_id,
            iid=movie_id
        )

        recommendations.append(
            (
                movie_id,
                pred.est
            )
        )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top_movies = recommendations[:top_n]

    result = []

    for movie_id, rating in top_movies:

        title = movies_df[
            movies_df["movie_id"] == movie_id
        ]["title"].values[0]

        result.append(
            {
                "movie": title,
                "predicted_rating": round(
                    rating,
                    2
                )
            }
        )

    return result

# ==========================================
# USER STATISTICS
# ==========================================

def get_user_stats(user_id):

    user_ratings = ratings_df[
        ratings_df["user_id"] == user_id
    ]

    movies_watched = len(user_ratings)

    avg_rating = round(
        user_ratings["rating"].mean(),
        2
    )

    watched_movie_ids = user_ratings[
        "movie_id"
    ].tolist()

    watched_movies = movies_df[
        movies_df["movie_id"].isin(
            watched_movie_ids
        )
    ]

    genre_columns = [
        "Action",
        "Adventure",
        "Animation",
        "Children",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western"
    ]

    genre_counts = watched_movies[
        genre_columns
    ].sum()

    favorite_genres = (
        genre_counts
        .sort_values(
            ascending=False
        )
        .head(3)
        .index
        .tolist()
    )

    return {
        "movies_watched": int(movies_watched),
        "avg_rating": float(avg_rating),
        "favorite_genres": favorite_genres
    }

# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    user_id = 15

    print(
        f"\nTop Recommendations for User {user_id}\n"
    )

    recs = get_top_recommendations(
        user_id=user_id,
        top_n=5
    )

    for movie in recs:

        print(
            movie["movie"],
            "->",
            movie["predicted_rating"]
        )

    print("\nUser Stats\n")

    print(
        get_user_stats(user_id)
    )