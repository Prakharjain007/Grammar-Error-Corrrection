import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Trainer, TrainingArguments

# Step 1: Install necessary libraries
# Make sure you've already installed transformers and torch using pip

torch.cuda.set_device(0)


# Step 2: Load the CoEdit tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
model = AutoModelForSeq2SeqLM.from_pretrained("grammarly/coedit-large")

print("01")

# Step 3: Load and preprocess your custom dataset

# Load your dataset from "data.csv" using pandas
data = pd.read_csv("Dataset\DATA.csv")

# Ensure your CSV file has columns named "input" and "output"

# Tokenize the input and output sentences
training_data = []

for index, row in data.iterrows():
    input_text = row["input"]
    output_text = row["output"] 

    # Tokenize the input and output sentences with padding and truncation
    tokenized_data = tokenizer(
        input_text,
        output_text,
        padding='max_length',  # Adjust this as needed
        truncation=True,
        return_tensors='pt',
    )

    training_example = {
        "input_ids": tokenized_data["input_ids"][0],
        "attention_mask": tokenized_data["attention_mask"][0],
        "labels": tokenized_data["input_ids"][0],  # Assuming you're using teacher forcing
    }

    training_data.append(training_example)

print("hello")


# Step 4: Define a data collator for sequence-to-sequence modeling
data_collator = DataCollatorForSeq2Seq(
    tokenizer=tokenizer,
    model=model,
    padding=True,
)

# Step 5: Define the training arguments and set the output directory
training_args = TrainingArguments(
    output_dir="./coedit_finetuned",
    overwrite_output_dir=True,
    num_train_epochs=2,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    max_steps=5000,
    save_steps=100,
    save_total_limit=2,
)

print("03")

# Step 6: Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset = training_data)

print("04")

# Step 7: Start training
trainer.train()

# Step 8: Save the trained model
trainer.save_model()
