import pandas as pd
import pickle

from surprise import Dataset
from surprise import Reader
from surprise import NMF

# ==========================================
# LOAD DATA
# ==========================================

columns = [
    "user_id",
    "movie_id",
    "rating",
    "timestamp"
]

train_df = pd.read_csv(
    "ml-100k/ml-100k/u1.base",
    sep="\t",
    names=columns
)

# ==========================================
# SURPRISE DATASET
# ==========================================

reader = Reader(rating_scale=(1, 5))

data = Dataset.load_from_df(
    train_df[["user_id", "movie_id", "rating"]],
    reader
)

trainset = data.build_full_trainset()

# ==========================================
# FINAL NMF MODEL
# ==========================================

model = NMF(
    n_factors=100,
    n_epochs=100,
    reg_pu=0.06,
    reg_qi=0.06,
    random_state=42
)

print("Training NMF Model...")

model.fit(trainset)

print("Training Complete!")

# ==========================================
# SAVE MODEL
# ==========================================

with open("nmf_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as nmf_model.pkl")