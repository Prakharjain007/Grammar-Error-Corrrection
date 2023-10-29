'''
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Replace 'gpt2' with the desired model name if needed
# Load model directly
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

# Example usage:
input_text = "I walk to the store and I bought milk"
corrected_sentence = correct_grammar(input_text)
print(corrected_sentence)


# Make sure to set the model to evaluation mode
model.eval()
'''




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

    # Find and print the changed words
    input_words = text.split()
    corrected_words = corrected_text.split()

    # Iterate over words and compare them
    for i, (input_word, corrected_word) in enumerate(zip(input_words, corrected_words)):
        if input_word != corrected_word:
            print(f"Word #{i+1}: Input: '{input_word}' -> Corrected: '{corrected_word}'")

    return corrected_text

# Example usage:
input_text = "I walk to the store and I bought milk"
corrected_sentence = correct_grammar(input_text)
print("Corrected Sentence:", corrected_sentence)
