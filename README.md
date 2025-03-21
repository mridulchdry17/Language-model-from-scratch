
# 📢 Project: LSTM-Based Email Language Model
### This project trains an LSTM-based language model on email data, allowing it to generate email-like text based on a given seed phrase.
```
Language_model_from_scratch/
│── data/
│   ├── emails.txt            # Extracted emails (used for training)
│   ├── processed_data.pkl     # Processed tokenized data
│
│── models/
│   ├── email_lm.h5            # Trained LSTM model
│
│
│───── extract_mail.py        # Extracts emails via IMAP
│───── preprocess_text.py     # Cleans & tokenizes data
│───── lstm_model.py          # Trains the LSTM model
│───── generate_text.py       # Generates text using the trained model
│
│── README.md                  # Project documentation
```
```
git clone https://github.com/mridulchdry17/Language_model_from_scratch.git
cd Language_model_from_scratch
```

### 📜 Steps to Train & Generate Text
#### 1️⃣ Extract Emails
##### Modify extract_mail.py with your email credentials, then run:
```
python scripts/extract_mail.py
```
##### This will save extracted emails to data/emails.txt.
#### 2️⃣ Preprocess Text Data
```
python scripts/preprocess_text.py
```
##### This tokenizes the text and saves processed data in data/processed_data.pkl.
#### 3️⃣ Train the LSTM Model
```
python scripts/lstm_model.py
```
##### ✔️ Trains the model and saves email_lm.h5 in models/.
#### 4️⃣ Generate Text
```
python scripts/generate_text.py
```
##### Outputs AI-generated email text based on a seed phrase.
#### 📝 Example Generated Text

```
Input: "Dear team, I hope you are"
Output: "Dear team, I hope you are doing well and looking forward to the next meeting."
```
##### (Results vary based on training data.)

### 📌 Future Improvements<br>
🔹 Add temperature-based sampling for more diverse text.<br>
🔹 Train on larger datasets for better generalization.<br>
🔹 Fine-tune using pretrained embeddings (Word2Vec, GloVe).<br>

