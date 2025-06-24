import torch
import shap


def explain_with_shap(model, tokenizer, tokens):
    # tokens: List[str]

    def forward_func(texts):
        # texts: List[List[str]]
        encodings = tokenizer(
            texts,
            is_split_into_words=True,
            return_tensors="pt",
            padding=True,
            truncation=True,
        )
        input_ids = encodings.input_ids
        attention_mask = encodings.attention_mask

        model.eval()
        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            probs = torch.softmax(logits, dim=-1)
        return probs.cpu().numpy()

    explainer = shap.Explainer(forward_func, tokenizer)

    # Here pass a list of list of tokens (batch size 1)
    shap_values = explainer([tokens])

    return shap_values
