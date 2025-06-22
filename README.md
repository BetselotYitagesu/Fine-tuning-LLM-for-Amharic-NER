✅ Task 1 & 2: Data Collection, Cleaning & Manual NER Annotation
📦 Task 1: Data Ingestion & Preprocessing

We collected Amharic e-commerce messages from 5 public Telegram channels using the Telethon Python library. These messages often include product names, prices, and store locations.
📡 Channels Scraped
Channel Name Messages
ShagerOnlineStore 89
Leyueqa 112
marakibrand 46
qnashcom 160
MerttEka 102
🔧 Preprocessing:

    Removed URLs, mentions, emojis, and non-Amharic characters.

    Preserved important text like numbers, prices, and Amharic punctuation.

    Output a cleaned message column for further annotation.

📂 Output Files

    Raw data: data/raw/*.csv

    Cleaned data: data/processed/*_clean.csv

    Scripts used:

        Scraper: scr/ingestion/scrape_telegram.py

        Cleaner: scr/preprocessing/preprocess_text.py

📝 Task 2: Manual NER Labeling in CoNLL Format

We manually labeled 30–50 cleaned messages using the standard CoNLL format, focusing on 3 key entity types for NER fine-tuning:
🏷️ Entity Types and Labels
Entity Tags
Product B-Product, I-Product
Price B-PRICE, I-PRICE
Location B-LOC, I-LOC
Other O
🧰 Tool Used:

Custom Python annotation interface:
scr/annotation/amharic_ner_annotator.py

    Prompts the user to label each token manually.

    Saves annotations in: amharic_ner_annotations.conll

📄 CoNLL Format Example:

Skechers B-Product  
archfit I-Product  
Price B-PRICE  
3400 I-PRICE  
birr I-PRICE  
አድራሻ B-LOC  
መክሲኮ I-LOC
