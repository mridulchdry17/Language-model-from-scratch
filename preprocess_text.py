import os
import numpy as np
import re
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer

def preprocess_data():
    # Get the absolute path to "data/" inside the project folder
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
    DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "data"))  

    # Ensure "data/" exists
    os.makedirs(DATA_DIR, exist_ok=True)  

    # Load emails from the correct "data/emails.txt"
    emails_file_path = os.path.join(DATA_DIR, "emails.txt")  

    # Check if `emails.txt` exists
    if not os.path.exists(emails_file_path):
        print(f"RROR: emails.txt not found at {emails_file_path}")
        return  # Exit if missing

    print(f"Found emails.txt at {emails_file_path}")

    # Read emails
    with open(emails_file_path, "r", encoding="utf-8") as f:
        text = f.read().lower()

    # Clean text
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Keep only letters and spaces
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces

    # Tokenization
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])

    # Convert to sequences
    data = tokenizer.texts_to_sequences([text])[0]

    if len(data) == 0:
        print("ERROR: No words found after tokenization!")
        return  # Exit if empty

    # Word index mappings
    word_to_idx = tokenizer.word_index
    idx_to_word = {v: k for k, v in word_to_idx.items()}

    # Prepare dataset
    sequence_length = 10
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i : i + sequence_length])  # Input sequence
        y.append(data[i + sequence_length])  # Next word prediction

    X = np.array(X)
    y = np.array(y)

    print(f"Dataset shape: {X.shape}, {y.shape}")

    # Save processed data in "data/"
    processed_data_path = os.path.join(DATA_DIR, "processed_data.pkl")  
    with open(processed_data_path, "wb") as f:
        pickle.dump((X, y, word_to_idx), f)

    print(f"Preprocessed data saved successfully at {processed_data_path}!")

    return X, y, word_to_idx

# Ensure script runs when executed directly
if __name__ == "__main__":  
    preprocess_data()
