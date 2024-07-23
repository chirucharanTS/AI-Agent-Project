import openai
import re
from config import OPENAI_API_KEY, MODEL_NAME, SLACK_BOT_TOKEN, SLACK_CHANNEL_ID
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from pdf_handler import extract_text_from_pdf

openai.api_key = OPENAI_API_KEY
client = WebClient(token=SLACK_BOT_TOKEN)

MAX_TEXT_LENGTH = 3000

def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length]
    return text

def extract_ceo_name(text):
    ceo_pattern = re.compile(r'([A-Z][a-z]+\s[A-Z][a-z]+)(?:\s*[,]?\s*CEO|(?:\s*CEO))')
    matches = ceo_pattern.findall(text)
    if matches:
        return matches[0]
    return "Data Not Available"

def get_answers_from_text(text, questions):
    answers = {}
    for question in questions:
        if "CEO" in question:
            answer = extract_ceo_name(text)
        else:
            truncated_text = truncate_text(text, MAX_TEXT_LENGTH)
            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Text: {truncated_text}\nQuestion: {question}"}
                ],
                max_tokens=100
            )
            answer = response.choices[0].message['content'].strip() if response.choices else "Data Not Available"
        answers[question] = answer
    return answers

def post_message_to_slack(message):
    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL_ID,
            text=message
        )
        return response
    except SlackApiError as e:
        assert e.response["error"]
