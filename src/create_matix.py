import pandas as pd

column_names = [
    "user_id",
    "movie_id",
    "rating",
    "timestamp"
]

train = pd.read_csv(
    "ml-100k/ml-100k/u1.base",
    sep="\t",
    names=column_names
)

user_movie_matrix = train.pivot(
    index="user_id",
    columns="movie_id",
    values="rating"
)

print(user_movie_matrix.shape)

print(user_movie_matrix.head())

#calculation sparsity 
# src/sparsity.py

import pandas as pd
import numpy as np

column_names = [
    "user_id",
    "movie_id",
    "rating",
    "timestamp"
]

train = pd.read_csv(
    "ml-100k/ml-100k/u1.base",
    sep="\t",
    names=column_names
)

R = train.pivot(
    index="user_id",
    columns="movie_id",
    values="rating"
)

num_users = R.shape[0]
num_movies = R.shape[1]

total_cells = num_users * num_movies
filled_cells = R.count().sum()

sparsity = 1 - (filled_cells / total_cells)

print("Users:", num_users)
print("Movies:", num_movies)
print("Ratings:", filled_cells)

print(f"Sparsity: {sparsity*100:.2f}%")


#preparing matrix for training
# src/prepare_matrix.py

import pandas as pd
import numpy as np

column_names = [
    "user_id",
    "movie_id",
    "rating",
    "timestamp"
]

train = pd.read_csv(
    "ml-100k/ml-100k/u1.base",
    sep="\t",
    names=column_names
)

R = train.pivot(
    index="user_id",
    columns="movie_id",
    values="rating"
)

R = R.fillna(0)

print(R.shape)

R = R.values

print(type(R))
print(R.shape)