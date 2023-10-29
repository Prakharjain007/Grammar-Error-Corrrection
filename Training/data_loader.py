# data_loader.py
import pandas as pd
from datasets import load_dataset
from torch.utils.data import Dataset, DataLoader
from transformers import T5Tokenizer
from sklearn.model_selection import train_test_split 


class GrammarDataset(Dataset):
    def __init__(self, dataset, tokenizer, max_token_length=64):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_token_length = max_token_length

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        example = self.dataset[index]
        input_text, target_text = example['input'], example['output']

        # Tokenize input and target sentences
        tokenized_input = self.tokenizer(input_text, padding='max_length', max_length=self.max_token_length, truncation=True, return_tensors='pt', return_attention_mask=True)
        tokenized_target = self.tokenizer(target_text, padding='max_length', max_length=self.max_token_length, truncation=True, return_tensors='pt', return_attention_mask=True)

        return {
            'input_ids': tokenized_input['input_ids'].squeeze(),
            'attention_mask': tokenized_input['attention_mask'].squeeze(),
            'labels': tokenized_target['input_ids'].squeeze()
        }

def load_data(file_path):
    # Load data from a CSV file into a DataFrame
    df = pd.read_csv(file_path)
    return df

def preprocess_data(data):
    # Perform any necessary data preprocessing
    # For example, you can clean and format the data here
    return data

def create_datasets(data, tokenizer):
    # Create train and test datasets
    train_df, test_df = train_test_split(data, test_size=0.10, shuffle=True)
    train_dataset = GrammarDataset(train_df, tokenizer)  # Pass the tokenizer here
    test_dataset = GrammarDataset(test_df, tokenizer)    # Pass the tokenizer here
    return train_dataset, test_dataset


'''if __name__ == "__main__":
    # Example usage:
    # Load data, preprocess it, and create datasets
    data = load_data("Dataset\c4_200m_1M.csv")
    preprocessed_data = preprocess_data(data)
    tokenizer = T5Tokenizer.from_pretrained("t5-small")  # Initialize the tokenizer
    train_dataset, test_dataset = create_datasets(preprocessed_data, tokenizer)  # Pass the tokenizer here
    print("done")'''
