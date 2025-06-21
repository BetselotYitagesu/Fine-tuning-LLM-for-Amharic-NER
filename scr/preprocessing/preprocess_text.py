import pandas as pd
import re


def clean_amharic_text(text):
    # Remove URLs, Emojis, Non-Amharic characters, punctuations etc.
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^\u1200-\u137F\s]+", "", text)  # Keep only Amharic range
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_dataframe(df_path):
    df = pd.read_csv(df_path)
    df['cleaned_message'] = df['message'].astype(str).apply(clean_amharic_text)
    return df[['channel', 'date', 'cleaned_message', 'views', 'id']]

# Example usage:
# df_clean = preprocess_dataframe('data/raw/ShagerOnlineStore.csv')
# df_clean.to_csv('data/processed/Shager_clean.csv', index=False)
