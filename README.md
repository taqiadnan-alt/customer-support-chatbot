# Customer Support Chatbot

An intent-based customer support chatbot built using TF-IDF text vectorization
and a Logistic Regression classifier, with a Streamlit chat interface.

## How it works
1. User message -> cleaned and converted to TF-IDF numeric vector
2. Logistic Regression model predicts the most likely intent
3. If confidence is below a threshold, the message is treated as "fallback"
   (instead of trusting a low-confidence guess)
4. A response is selected for the predicted intent

## Files
- `training_data.py` - example phrases for each of the 10 supported intents
- `chatbot.py` - trains the TF-IDF + Logistic Regression model, exposes `chatbot_reply()`
- `responses.py` - maps each intent to possible bot responses
- `app.py` - Streamlit chat interface

## Supported intents
- greeting
- order_status
- refund_request
- complaint
- shipping_time
- goodbye
- fallback (catch-all for unrelated/unclear messages)
- cancel_order
- payment_issue
- product_availability

## How to run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Development notes / lessons learned
- Started with 7 intents, expanded to 10. Adding intents increases confusion
  risk between similar categories (e.g. cancel_order vs order_status,
  cancel_order vs refund_request), so confidence naturally drops as more
  intents are added.
- Used an active-learning-style approach: ran the model on new test
  sentences, found misclassifications, then added targeted training
  examples based on the specific failures observed (rather than
  guessing blindly what data was missing).
- Confidence threshold was tuned down from 30% -> 18% -> 15% as the
  number of intents grew, since random-guess baseline drops as
  intent count increases (~14% for 7 intents, ~10% for 10 intents).

## Possible improvements
- Add more training examples per intent to increase model confidence further
- Add slot-filling (e.g. asking for and storing an order ID)
- Try embeddings (e.g. sentence-transformers) instead of TF-IDF for better
  semantic understanding of paraphrased sentences
- Add a "speak_to_human" escalation intent
