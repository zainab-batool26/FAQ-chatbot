import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

STOP_WORDS = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Map similar words to one canonical word, applied to both FAQs and user input
SYNONYMS = {
    'cash': 'money', 'fund': 'money', 'payment': 'money', 'refund': 'money',
    'stolen': 'lost', 'missing': 'lost', 'theft': 'lost',
    'start': 'open', 'create': 'open', 'new': 'open',
    'send': 'transfer', 'wire': 'transfer',
    'freeze': 'block', 'disable': 'block',
    'update': 'change', 'modify': 'change', 'reset': 'change',
}

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in STOP_WORDS and len(t) > 1]
    tokens = [SYNONYMS.get(t, t) for t in tokens]
    return ' '.join(tokens)

with open('faqs.json', encoding='utf-8') as f:
    faqs = json.load(f)

processed_questions = [preprocess(item['question']) for item in faqs]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

THRESHOLD = 0.35

def get_answer(user_input):
    processed = preprocess(user_input)
    if not processed:
        return "Please ask a question with some words in it."

    user_vector = vectorizer.transform([processed])
    scores = cosine_similarity(user_vector, question_vectors)[0]
    best_index = scores.argmax()
    print(f"[debug] score={float(scores[best_index]):.2f} matched='{faqs[best_index]['question']}'")

    if scores[best_index] < THRESHOLD:
        return "Sorry, I don't have an answer for that. Try rephrasing your question."
    return faqs[best_index]['answer']

if __name__ == '__main__':
    print("FAQ Chatbot. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'quit':
            break
        print("Bot:", get_answer(user_input), "\n")