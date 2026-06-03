import os
import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

def send_email():
    msg = MIMEText("""
🚨 Polymarket Trend Reversal Alert Test

This is a test email.

If you received this, the email alert system is working.
""")

    msg["Subject"] = "Test: Polymarket Alert System"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    send_email()
