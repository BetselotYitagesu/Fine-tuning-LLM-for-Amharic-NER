# amharic_ner_annotator.py

from transformers import BertTokenizer

# Load multilingual BERT tokenizer (includes Amharic)
tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")

# Predefined labels
LABELS = [
    "B-LOC", "I-LOC", "B-FAC", "I-FAC",
    "B-ADDR", "I-ADDR", "B-BIZINFO", "I-BIZINFO", "O"
]


def annotate_sentence(text):
    tokens = tokenizer.tokenize(text)
    annotations = []

    print("\nAnnotate each token with a label from the following:")
    print(f"LABELS: {LABELS}")
    print("Type correct label (e.g., B-LOC), or press Enter for default 'O'\n")

    for token in tokens:
        print(f"Token: {token}")
        label = input("Label: ").strip()
        if label not in LABELS:
            label = "O"
        annotations.append((token, label))

    return annotations


def write_conll(annotated_data, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for sentence in annotated_data:
            for token, label in sentence:
                f.write(f"{token} {label}\n")
            f.write("\n")  # Sentence separator


def main():
    print("📌 Amharic NER Annotator – Manual Tagging Interface")
    print("Enter Amharic sentence(s) to annotate. Type 'exit' to finish.\n")

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
        print("⚠️ No data annotated.")


if __name__ == "__main__":
    main()
