import pandas as pd
import re

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def clean_subscribers(csv_path):
    df = pd.read_csv(csv_path)

    before = len(df)

    df = df.drop_duplicates(subset="email")

    df = df[df["email"].apply(valid_email)]

    after = len(df)

    return df, before, after