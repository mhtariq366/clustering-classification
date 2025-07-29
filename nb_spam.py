import pandas as pd

df = pd.read_csv("datasets/spam.csv", encoding="latin-1")
df = df.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"])
df = df.rename(columns={"v1":"Label", "v2":"Text"})

