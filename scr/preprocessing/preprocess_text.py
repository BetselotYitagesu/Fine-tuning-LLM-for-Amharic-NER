"""Improved Amharic + English Price-Aware Preprocessing"""

import re
import pandas as pd


def clean_amharic_text(text: str) -> str:
    # Normalize different dash characters
    text = text.replace("\u2013", "-").replace("\u2014", "-")

    # Remove URLs and @mentions
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)

    # TEMPORARILY protect price expressions (Amharic & English forms)
    price_patterns = re.findall(
        r"(ዋጋ\s*\d+\s*ብር"
        r"|በ\s*\d+\s*ብር"
        r"|\d+\s*ብር"
        r"|Price\s*\d+\s*birr"
        r"|price\s*\d+\s*birr)",
        text
    )

    placeholders = [f"__PRICE_{i}__" for i in range(len(price_patterns))]
    for pattern, placeholder in zip(price_patterns, placeholders):
        text = text.replace(pattern, placeholder)

    # Allow Amharic, Latin (A-Z, a-z), digits, selected punctuation
    text = re.sub(r"[^\u1200-\u137Fa-zA-Z0-9፡።.,:/\-()\s]", "", text)

    # Restore protected price phrases
    for placeholder, pattern in zip(placeholders, price_patterns):
        text = text.replace(placeholder, pattern)

    # Normalize whitespace
    return re.sub(r"\s+", " ", text).strip()


def preprocess_dataframe(df_path: str) -> pd.DataFrame:
    """Reads a CSV and returns cleaned messages."""
    df = pd.read_csv(df_path)
    df['cleaned_message'] = df['message'].astype(str).apply(clean_amharic_text)
    return df[['channel', 'date', 'cleaned_message', 'views', 'id']]


# Example usage:
# df_clean = preprocess_dataframe("data/raw/ethio_brand_collection.csv")
# df_clean.to_csv("data/processed/ethio_brand_clean.csv", index=False)
