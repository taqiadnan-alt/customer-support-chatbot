"""
Day 3: The full chatbot brain.

Pipeline: user message -> TF-IDF -> predict intent -> check confidence -> respond

If confidence is below our threshold, we DON'T trust the prediction -
we treat it as fallback instead. This avoids the bot confidently giving
a wrong answer.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from training_data import training_data
from responses import get_response

# --- Train the model (same as Day 2) ---
texts, labels = [], []
for intent, examples in training_data.items():
    for example in examples:
        texts.append(example)
        labels.append(intent)

vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

# --- Confidence threshold ---
# If the model's top confidence is below this, we don't trust it.
# We now have 10 intents (random-guess baseline ~10%), and more intents
# means more competition between categories, so confidence naturally
# runs lower than with 7 intents. 15% keeps us above random guessing
# while accounting for our still-small training set.
CONFIDENCE_THRESHOLD = 0.15


def chatbot_reply(message):
    """Takes a raw user message, returns (intent, confidence, reply)."""
    vector = vectorizer.transform([message])
    predicted_intent = model.predict(vector)[0]
    confidence = max(model.predict_proba(vector)[0])

    if confidence < CONFIDENCE_THRESHOLD:
        intent_used = "fallback"
    else:
        intent_used = predicted_intent

    reply = get_response(intent_used)
    return predicted_intent, confidence, reply


if __name__ == "__main__":
    test_messages = [
        "hi there",
        "where's my stuff",
        "this is broken, I want my money back",
        "how long till delivery",
        "asdkj random gibberish",
        "thanks bye",
        # New intents:
        "I don't want this order anymore, please stop it",
        "my card was charged but the order doesn't show",
        "do you have this in blue",
        # Tricky overlap test: cancel vs refund
        "I want to return this and get my money back",
        "can you stop my order before it ships",
    ]

    print("=== Chatbot Test Run ===\n")
    for msg in test_messages:
        intent, conf, reply = chatbot_reply(msg)
        print(f"You: {msg}")
        print(f"  [predicted intent: {intent} | confidence: {conf*100:.1f}%]")
        print(f"Bot: {reply}\n")
