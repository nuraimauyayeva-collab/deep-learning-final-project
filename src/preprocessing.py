import pandas as pd
import re
from sklearn.model_selection import train_test_split

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def load_data():

    fake_df = pd.read_csv("Fake.csv")
    true_df = pd.read_csv("True.csv")

    fake_df["label"] = 0
    true_df["label"] = 1

    df = pd.concat([fake_df, true_df])

    df = df.sample(10000, random_state=42)

    df["clean_text"] = df["text"].apply(clean_text)

    return df

def split_data(df):

    X = df["clean_text"]
    y = df["label"]

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
