# AI-Agent-Project
# AI Agent for PDF-Based QA on Slack

## Problem Statement

This project creates an AI agent capable of answering questions based on the content of a large PDF document and posting the results on Slack. The agent leverages OpenAI's large language models (LLMs) and is implemented without relying on pre-built frameworks like Langchain or Llama Index.

## Project Overview

The AI agent performs the following tasks:

- **Extracts text from a PDF file.**
- **Answers a list of questions based on the extracted text.**
- **Posts the results on Slack.**

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   
2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows

3. **Install Dependencies**

   Make sure you have pip installed and use the following command:
   
   ```bash
   pip install -r requirements.txt

5. **Set Up Environment Variables**

   Create a .env file in the root directory with the following content:
   
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   SLACK_BOT_TOKEN=your_slack_bot_token
   SLACK_CHANNEL_ID=your_slack_channel_id

 ## Usage
 
 1. **Run the Flask Application**

     Start the Flask server with the following command:
     ```bash
     python main.py

 2.**Interact with the Slack Bot**

   Upload a PDF File: Upload the PDF file to the Slack channel where the bot is active.
   Ask Questions: Post questions in the Slack channel.
   Receive Answers: The bot will process the PDF and answer the questions, posting the results in the same channel.

## Code Structure

    config.py: Configuration settings, including API keys and model names.
    main.py: The main Flask application handling Slack events and processing PDF files.
    pdf_handler.py: Functions for extracting text from PDF files.
    qa_system.py: Functions for querying the extracted text and posting results to Slack.

## Improving Accuracy and Quality

   Preprocessing: Improve text extraction from PDF by preprocessing and cleaning the text to handle different formats and layouts.
   Error Handling: Enhance error handling to manage edge cases and unexpected inputs more gracefully.
   Model Tuning: Fine-tune the OpenAI model or experiment with different prompts to improve answer accuracy.

## Modularity and Scalability
  Modular Functions: The code is divided into modules for handling configuration, PDF processing, and QA to promote readability and maintainability.
  Scalability: Consider using cloud services or serverless functions to handle scalability in a production environment.
  Unit Testing: Implement unit tests to ensure code reliability and facilitate future changes.

## Screenshot
![image](https://github.com/user-attachments/assets/7de42175-57e4-43a2-9333-577ac043adf7)

## Notes
The API keys provided are for demonstration purposes only. Ensure to use your own keys in production.
The code is designed for the gpt-3.5-turbo-0125 model as specified.

## Questions
If you have any questions, feel free to reach out to us at vajara369chiru@gmail.com.



