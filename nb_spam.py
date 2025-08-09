import pandas as pd

# reading dataset from csv file
df = pd.read_csv("datasets/spam.csv", encoding="latin-1")

# drop columns 2, 3 and 4.
df = df.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"])

# renaming the text and given label columns
df = df.rename(columns={"v1":"Label", "v2":"Text"})

