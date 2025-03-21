import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ✅ Load the trained LSTM model
model = load_model("models/email_lm.h5")  

# ✅ Load word mappings
with open("data/processed_data.pkl", "rb") as f:
    _, _, word_to_idx = pickle.load(f)

# ✅ Create index-to-word mapping
idx_to_word = {v: k for k, v in word_to_idx.items()}

# ✅ Define the text generation function
def generate_text(model, word_to_idx, seed_text, max_words=12):
    """
    Generates text using the trained LSTM model.
    
    Args:
    - model: Trained LSTM model
    - word_to_idx: Dictionary mapping words to indices
    - seed_text: Starting words for text generation
    - max_words: Number of words to generate
    
    Returns:
    - Generated text string
    """
    for _ in range(max_words):
        # Convert seed text to sequence
        sequence = [word_to_idx.get(word, 0) for word in seed_text.split()]
        sequence = pad_sequences([sequence], maxlen=10, truncating="pre")  # Keep last 10 words

        # Predict next word index
        predicted_index = np.argmax(model.predict(sequence), axis=-1)[0]

        # Convert index back to word
        next_word = idx_to_word.get(predicted_index, "")  # Handle unknown words
        if next_word == "":
            break  # Stop if unknown word generated

        # Append word to seed text
        seed_text += " " + next_word

    return seed_text

# ✅ Example usage
seed_text = "Good Morning "
generated_text = generate_text(model, word_to_idx, seed_text)
print("Generated Text:", generated_text)
