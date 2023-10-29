# config.py
import torch
from transformers import T5Tokenizer 


# Data-related configurations
DATA_FILE_PATH = "Dataset\daaaaata.csv"  # Path to your dataset file
MAX_TOKEN_LENGTH = 64  # Maximum token length for input and target sequences
RANDOM_SEED = 42  # Random seed for reproducibility
BATCH_SIZE = 16  # Batch size for training

# Model-related configurations
MODEL_NAME = 't5-base'  # Pre-trained model name or path
MODEL_OUTPUT_DIR = "/content/drive/MyDrive/c4_200m/weights"  # Directory to save trained model weights
tokenizer = T5Tokenizer.from_pretrained("t5-base")


# Training-related configurations
LEARNING_RATE = 2e-5  # Learning rate for training
NUM_EPOCHS = 1  # Number of training epochs
WEIGHT_DECAY = 0.01  # Weight decay for regularization
SAVE_TOTAL_LIMIT = 2  # Maximum number of checkpoints to keep
EVALUATION_STRATEGY = "steps"  # Evaluation strategy during training
FP16 = True  # Enable mixed-precision training
GRADIENT_ACCUMULATION_STEPS = 6  # Number of gradient accumulation steps
EVAL_STEPS = 500  # Evaluate every N steps during training
SAVE_STEPS = 500  # Save model checkpoints every N steps
LOAD_BEST_MODEL_AT_END = True  # Whether to load the best model at the end of training

# Inference-related configurations
INFERENCE_MODEL_PATH = 'deep-learning-analytics/GrammarCorrector'  # Pre-trained model name or path
TORCH_DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'  # Device for inference

# Other configurations
LOGGING_DIR = "/logs"  # Directory for log files
REPORT_TO = None  # Reporting destination (e.g., Weights & Biases)

# Add any additional configurations you need for your specific project
