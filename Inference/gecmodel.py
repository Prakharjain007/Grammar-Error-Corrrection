import sys
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
model = AutoModelForSeq2SeqLM.from_pretrained("grammarly/coedit-large")
 
def correct_grammar(text):
    # Tokenize the input text
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Generate corrected text
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the output to get the corrected sentence
    corrected_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return corrected_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gecmodel.py <spoken_text>")
        sys.exit(1)

    spoken_text = sys.argv[1]
    corrected_text = correct_grammar(spoken_text)
    print(corrected_text)
