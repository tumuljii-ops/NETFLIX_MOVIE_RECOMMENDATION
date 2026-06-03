# 🎬 Netflix Recommendation System using Matrix Factorization

## Overview

This project is an end-to-end Movie Recommendation System built using Matrix Factorization techniques on the MovieLens 100K dataset.

The system learns hidden (latent) preferences of users and movies from historical ratings and generates personalized movie recommendations.

The project includes:

* Matrix Factorization based recommendation engine
* User analytics and statistics
* FastAPI backend
* Streamlit frontend
* Docker containerization

---

## Problem Statement

Modern streaming platforms contain thousands of movies and users often struggle to discover relevant content.

The goal of this project is to build a recommendation engine that can:

1. Learn user preferences from historical ratings.
2. Predict ratings for unseen movies.
3. Recommend the most relevant movies to each user.

---

## Dataset

Dataset Used: MovieLens 100K

Dataset Statistics:

* Users: 943
* Movies: 1682
* Ratings: 100,000+
* Sparsity: ~94%

Each rating contains:

* User ID
* Movie ID
* Rating (1–5)

---

## Matrix Factorization

The recommendation problem is modeled as a User–Item Rating Matrix.

R ≈ P × Qᵀ

Where:

* R = User–Movie Rating Matrix
* P = User Latent Factor Matrix
* Q = Movie Latent Factor Matrix

The model learns hidden representations of users and movies.

Example latent features:

* Action preference
* Comedy preference
* Romance preference
* Drama preference

Predicted rating:

r̂(u,i) = μ + bᵤ + bᵢ + Pᵤ·Qᵢ

Where:

* μ = Global Average Rating
* bᵤ = User Bias
* bᵢ = Movie Bias
* Pᵤ = User Latent Vector
* Qᵢ = Movie Latent Vector

---

## Model Training

Training techniques used:

* Matrix Factorization
* Regularization
* Hyperparameter Tuning
* RMSE Evaluation

Final deployed model:

* Non-Negative Matrix Factorization (NMF)

Evaluation Metric:

* RMSE (Root Mean Squared Error)

Final RMSE:

* ~0.94 on MovieLens 100K

---

## System Architecture

MovieLens Dataset

↓

Matrix Factorization Model

↓

FastAPI Backend

↓

Streamlit Frontend

↓

Docker Container

---

## Features

### User Statistics

For a given User ID:

* Movies Watched
* Average Rating
* Favorite Genres

### Personalized Recommendations

The system:

1. Finds movies not rated by the user.
2. Predicts ratings for unseen movies.
3. Sorts predictions in descending order.
4. Returns Top 5 recommendations.

### REST APIs

Available endpoints:

* GET /
* GET /recommend/{user_id}
* GET /user_stats/{user_id}

### Interactive Dashboard

Built using Streamlit.

Users can:

* Enter User ID
* View statistics
* Get Top 5 recommendations

---

## Technology Stack

Backend:

* FastAPI

Frontend:

* Streamlit

Machine Learning:

* Matrix Factorization (NMF)
* Scikit-Surprise

Data Processing:

* Pandas
* NumPy

Containerization:

* Docker

---

## Project Structure

NETFLIX_RECOMMENDATION/

├── frontend/

├── ml-100k/

├── src/

│ ├── app.py

│ ├── recommend.py

│ └── train.py

├── nmf_model.pkl

├── requirements.txt

├── Dockerfile

└── README.md

---

## Deployment

The application is containerized using Docker and can be deployed on cloud platforms such as:

- Render

Deployment Workflow:

GitHub Repository
      ↓
Docker Image
      ↓
Cloud Platform
      ↓
Live Recommendation Service

The deployed application provides:

- User Statistics
- Personalized Movie Recommendations
- REST APIs via FastAPI
- Interactive Streamlit Dashboard

## Author

Tumul Singh

B.Tech Information Technology

National Institute of Technology Kurukshetra
