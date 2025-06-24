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

ask 3: Model Evaluation

    Evaluated the fine-tuned XLM-RoBERTa NER model using the seqeval metric for entity-level precision, recall, and F1-score.

    Implemented evaluation code to map predicted token labels back to entities and compared with ground truth.

    Generated detailed classification reports to identify model strengths and weaknesses on PRODUCT, PRICE, and LOCATION entities.

    Evaluated on test splits of the dataset and saved performance metrics for reference.

Task 4: Model Inference

    Developed an inference pipeline to predict named entities on new Amharic Telegram messages.

    Implemented tokenization with proper word alignment to handle subword token predictions.

    Converted model logits into entity labels with confidence scores.

    Designed functions to post-process predictions, extracting entity spans from token-level outputs.

    Validated inference results qualitatively with sample real-world Telegram messages.

Task 5: Model Interpretability

    Integrated SHAP and LIME to explain model predictions.

    Created scripts in src/interpretability/interprete_model.py.

    Generated explanation plots (.png) for example predictions.

    Included interpretability results and graphs in README.

Task 6: FinTech Vendor Scorecard

    Developed src/vendor_analysis/vendor_score.py to aggregate vendor data.

    Calculated metrics: posts/week, average views/post, average price, lending score.

    Output saved to vendor_scorecard.csv.

    Summary table of vendor scores added to README for business insights.

Project Structure

data/
├─ raw/
└─ processed/
models/
└─ xlm-roberta-ner/
notebooks/
├─ 01_eda.ipynb
├─ 02_labeling.ipynb
├─ 03_finetuning.ipynb
├─ 04_interprete.ipynb
└─ 05_vendor_score.ipynb
src/
├─ annotation/
│ └─ amharic_ner_annotation.py
├─ ingestion/
│ └─ scrape_telegram.py
├─ interpretability/
│ └─ interprete_model.py
└─ vendor_analysis/
└─ vendor_score.py

How to Run

    Fine-tune model: run notebooks/03_finetuning.ipynb.

    Generate interpretability plots: run notebooks/04_interprete.ipynb.

    Calculate vendor scorecard: run notebooks/05_vendor_score.ipynb.

    Use saved model for inference in scripts under src/.

Requirements

    Python 3.8+

    transformers, datasets, seqeval, shap, lime, torch

    Other dependencies listed in requirements.txt
