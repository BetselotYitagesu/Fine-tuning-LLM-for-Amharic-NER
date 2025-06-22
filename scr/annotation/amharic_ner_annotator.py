""" amharic_ner_annotator.py """

# from transformers import BertTokenizer
# from transformers import AutoTokenizer
# tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("Davlan/afro-xlmr-base")

# Load multilingual BERT tokenizer that includes Amharic
# tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")

# Updated labels based on task 2
LABELS = [
    "B-Product", "I-Product",
    "B-LOC", "I-LOC",
    "B-PRICE", "I-PRICE",
    "O"
]


def annotate_sentence(text):
    """Annotatin Sentence mehtod """
    tokens = tokenizer.tokenize(text)
    annotations = []

    print("\n🔍 Annotate each token with a label:")
    print(f"Available LABELS: {LABELS}")
    print("Press Enter to assign 'O' (non-entity) label by default.\n")

    for token in tokens:
        print(f"🟦 Token: {token}")
        label = input("🏷️  Label: ").strip()
        if label not in LABELS:
            label = "O"
        annotations.append((token, label))

    return annotations


def write_conll(annotated_data, output_file):
    with open(output_file, "a", encoding="utf-8") as f:
        for sentence in annotated_data:
            for token, label in sentence:
                f.write(f"{token} {label}\n")
            f.write("\n")  # Sentence separator


def main():
    """The main function"""
    print("📌 Amharic NER Annotator – Manual Tagging Interface")
    print("Type Amh sentences to annotate. Type 'exit' to finish & save.\n")

    output_file = "amharic_ner_annotations.conll"
    all_data = []

    while True:
        text = input("📥 Enter Amharic Sentence: ").strip()
        if text.lower() == "exit":
            break
        annotations = annotate_sentence(text)
        all_data.append(annotations)

    if all_data:
        write_conll(all_data, output_file)
        print(f"\n✅ Annotation saved to: {output_file}")
    else:
        print("⚠️ No data was annotated. Exiting...")


if __name__ == "__main__":
    main()
