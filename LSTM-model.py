import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from preprocess_text import preprocess_data  # Import function

# Load preprocessed data
X, y, word_to_idx = preprocess_data()
print("Preprocessed data loaded successfully!")

# Define model
model = Sequential([
    Embedding(len(word_to_idx) + 1, 128, input_length=X.shape[1]),
    LSTM(256, return_sequences=True),
    LSTM(256),
    Dense(len(word_to_idx) + 1, activation="softmax")
])

# Compile model
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train model
model.fit(X, y, epochs=10, batch_size=64)

# Save model
model.save("../models/email_lm.h5")  # Save model in `models/`
print("Training complete!")
