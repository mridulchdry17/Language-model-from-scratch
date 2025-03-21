import os
import imaplib
import email
from email.header import decode_header

# ✅ Get current directory and ensure "data/" exists inside the project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get script's directory
DATA_DIR = os.path.join(BASE_DIR, "data")  # Ensure "data/" is inside project
os.makedirs(DATA_DIR, exist_ok=True)  # ✅ Create "data/" if it doesn't exist

# Connect to Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("mror1822@gmail.com", "qbhq hguk ivnx quuo")  

mail.select("inbox")

# Fetch all email IDs
status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()

# Fetch and parse emails
emails = []
for email_id in email_ids[:100]:  # Limit to 100 emails
    email_id_str = email_id.decode()
    _, msg_data = mail.fetch(email_id_str, "(RFC822)")

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])

            # Decode subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            # Extract email body
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                        break
            else:
                body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

            emails.append(subject + "\n" + body)

# ✅ Save emails to "data/emails.txt" INSIDE the project folder
emails_file_path = os.path.join(DATA_DIR, "emails.txt")
with open(emails_file_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(emails))

print(f"Emails saved successfully in {emails_file_path}!")