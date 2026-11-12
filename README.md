# FAQ Chatbot

A web-based FAQ assistant built with Python and Flask. Visitors type a question, and the bot finds the most similar FAQ by meaning and returns its answer in a chat window.

## Features

- Chat interface in the browser, with suggestion buttons for common questions
- Semantic matching with sentence embeddings, so different wording can still find the right answer
- Text preprocessing with NLTK (lowercasing, cleaning, and tokenizing)
- Confidence threshold that returns a fallback message when no FAQ is a good match
- FAQs stored in a single JSON file, so the bot can be reused for any product

## How It Works

1. Each FAQ question is cleaned with NLTK and converted into a vector by `all-MiniLM-L6-v2`, a small sentence-embedding model.
2. When a user sends a message, it goes through the same cleaning and embedding steps.
3. Cosine similarity compares the message with every FAQ question.
4. The answer for the closest question is returned if its score passes the threshold. Otherwise, the bot asks the user to rephrase.

## Tech Stack

- Python 3
- Flask (web server and chat endpoint)
- NLTK (text preprocessing)
- sentence-transformers (semantic embeddings)
- HTML, CSS, and JavaScript (chat interface)

## Project Structure

```
faq-chatbot/
├── app.py           # Flask server and /chat endpoint
├── chatbot.py       # Preprocessing, embeddings, and matching
├── faqs.json        # Questions and answers
├── .gitignore       # Excludes venv/ and __pycache__/
└── static/
    ├── index.html   # Chat page
    ├── style.css    # Chat styling
    └── script.js    # Chat logic in the browser
```
## Getting Started

```bash
git clone https://github.com/zainab-batool26/FAQ-chatbot.git
cd FAQ-chatbot
python -m venv venv
venv\Scripts\activate        # On Mac/Linux: source venv/bin/activate
pip install flask nltk scikit-learn sentence-transformers
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

The first run downloads the embedding model (about 90 MB), so it may take a few minutes.

## Customizing the FAQs

Edit `faqs.json` and add entries in this format:

```json
{
  "question": "How do I reset my password?",
  "answer": "Select Forgot Password on the login screen and follow the steps."
}
```

Restart `python app.py` after making changes. The sample content is a fictional bank, Example Bank, so you can replace it with any topic.

## Limitations

- The bot only answers questions covered by its FAQ list.
- It returns a fallback message when no match is strong enough, so very vague questions may not get an answer.
- It is a demonstration project and does not connect to real account data.

## What I Learned

- Text preprocessing with NLTK and why it matters for matching
- Turning text into vectors and comparing them with cosine similarity
- Tuning a similarity threshold based on real test questions
- Building a Flask API and connecting it to a browser front end

## Author

Zainab Batool · [GitHub](https://github.com/zainab-batool26)
