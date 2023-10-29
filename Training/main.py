# main.py
import torch
from data_loader import load_data, preprocess_data, create_datasets
from train import train_model, compute_metrics
from inference import load_trained_model, correct_grammar
import config
from transformers import T5Tokenizer


if __name__ == "__main__":
    # Load data
    data = load_data(config.DATA_FILE_PATH)
    print('01')
    
    # Preprocess data
    preprocessed_data = preprocess_data(data)
    print('02')

    
    # Create datasets
    tokenizer = T5Tokenizer.from_pretrained(config.MODEL_NAME)
    print('03')

    
    # Create datasets, passing the tokenizer argument
    train_dataset, test_dataset = create_datasets(preprocessed_data, tokenizer)
    print('04') 

    
    # Train the model
    trained_model = train_model(train_dataset, test_dataset)
    print('05')

    
    # Save the trained model
    #save_model(trained_model, config.MODEL_OUTPUT_DIR)
    
    # Load the trained model for inference
    inference_model, inference_tokenizer = load_trained_model(config.INFERENCE_MODEL_PATH, config.TORCH_DEVICE)
    print('06')

    
    # Perform inference to correct grammar
    input_text = 'He are moving here.'  # Replace with your input sentence
    num_return_sequences = 2  # Number of corrected sequences to generate
    corrected_sentences = correct_grammar(inference_model, inference_tokenizer, input_text, num_return_sequences)
    
    # Print corrected sentences
    for i, corrected_sentence in enumerate(corrected_sentences):
        print(f'Correction {i+1}: {corrected_sentence}')
