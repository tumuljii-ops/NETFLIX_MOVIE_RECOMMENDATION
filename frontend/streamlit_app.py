import streamlit as st
import requests

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# ==========================================
# TITLE
# ==========================================

st.title("🎬 Netflix Recommendation System")

st.write(
    "Get personalized movie recommendations "
    "using Matrix Factorization (NMF)."
)

# ==========================================
# USER INPUT
# ==========================================

user_id = st.number_input(
    "Enter User ID",
    min_value=1,
    max_value=943,
    value=15
)

# ==========================================
# BUTTON
# ==========================================

if st.button("Recommend Movies"):

    # --------------------------------------
    # USER STATS API
    # --------------------------------------

    stats_url = (
        f"https://netflix-movie-recommendation-3.onrender.com"
    )

    stats_response = requests.get(
        stats_url
    )

    stats = stats_response.json()

    st.subheader("📊 User Statistics")

    st.write(
        f"**Movies Watched:** "
        f"{stats['stats']['movies_watched']}"
    )

    st.write(
        f"**Average Rating:** "
        f"{stats['stats']['avg_rating']}"
    )

    st.write(
        f"**Favorite Genres:** "
        f"{', '.join(stats['stats']['favorite_genres'])}"
    )

    st.divider()

    # --------------------------------------
    # RECOMMENDATION API
    # --------------------------------------

    rec_url = (
        f"http://127.0.0.1:8000/recommend/{user_id}"
    )

    rec_response = requests.get(
        rec_url
    )

    recs = rec_response.json()

    st.subheader(
        "🎥 Top 5 Recommendations"
    )

    for movie in recs[
        "recommendations"
    ]:

        st.write(
            f"⭐ {movie['movie']}"
        )

        st.write(
            f"Predicted Rating: "
            f"{movie['predicted_rating']}"
        )

        st.write("---")