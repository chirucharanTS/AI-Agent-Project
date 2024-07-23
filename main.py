import os
from pdf_handler import extract_text_from_pdf
from qa_system import get_answers_from_text, post_message_to_slack
from config import SLACK_CHANNEL_ID

# Load PDF file
pdf_path = 'handbook.pdf'
pdf_text = extract_text_from_pdf(pdf_path)

# Define questions
questions = [
    "What is the name of the company?",
    "Who is the CEO of the company?",
    "What is their vacation policy?",
    "What is the termination policy?"
]

# Get answers
answers = get_answers_from_text(pdf_text, questions)

# Prepare message for Slack
message = ""
for question, answer in answers.items():
    message += f"Q: {question}\nA: {answer}\n\n"

# Post results to Slack
post_message_to_slack(message)
