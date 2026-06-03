from fastapi import FastAPI

from Backend.recommend import (
    get_top_recommendations,
    get_user_stats
)

app = FastAPI(
    title="Netflix Recommendation API"
)

@app.get("/")
def home():

    return {
        "message":
        "Netflix Recommendation System API"
    }

@app.get("/recommend/{user_id}")
def recommend(user_id: int):

    return {
        "user_id": user_id,
        "recommendations":
        get_top_recommendations(user_id)
    }

@app.get("/user_stats/{user_id}")
def user_stats(user_id: int):

    return {
        "user_id": user_id,
        "stats":
        get_user_stats(user_id)
    }