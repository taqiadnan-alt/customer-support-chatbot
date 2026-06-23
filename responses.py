"""
Day 3: Mapping each intent to a response.

Why a LIST of responses per intent instead of just one?
-> So the bot doesn't sound robotic by repeating the exact same sentence
   every single time someone has the same intent. We'll pick one at random.
"""
import random

responses = {
    "greeting": [
        "Hi there! How can I help you today?",
        "Hello! What can I do for you?",
        "Hey! How can I assist you?",
    ],
    "order_status": [
        "Sure, I can help with that. Could you share your order ID so I can check the status?",
        "Let me check that for you — what's your order number?",
    ],
    "refund_request": [
        "I'm sorry to hear that. I can help start a refund — could you share your order ID?",
        "No problem, let's get that sorted. Can you tell me your order number so I can process the refund?",
    ],
    "complaint": [
        "I'm really sorry about that experience. Could you tell me more about what went wrong?",
        "That's not the experience we want for you. Can you share your order ID so I can escalate this?",
    ],
    "shipping_time": [
        "Standard shipping usually takes 3-5 business days. Express shipping takes 1-2 days.",
        "Delivery typically takes 3-5 business days depending on your location.",
    ],
    "goodbye": [
        "Glad I could help! Have a great day.",
        "You're welcome! Take care.",
    ],
    "fallback": [
        "Hmm, I'm not sure I understood that. Could you rephrase your question?",
        "Sorry, I didn't quite catch that. Could you tell me more about what you need help with?",
    ],
    "cancel_order": [
        "I can help cancel that. Could you share your order ID so I can process the cancellation?",
        "No problem — please share your order number and I'll cancel it for you, as long as it hasn't shipped yet.",
    ],
    "payment_issue": [
        "I'm sorry about that. Could you share your order ID and the payment method used, so I can look into it?",
        "That sounds frustrating — let's get it sorted. Can you tell me your order number and when the charge happened?",
    ],
    "product_availability": [
        "Let me check that for you — could you tell me the exact product name or ID?",
        "Sure, I can check stock and size/color options. What's the product you're asking about?",
    ],
}

def get_response(intent):
    """Pick a random response for the given intent."""
    return random.choice(responses[intent])


if __name__ == "__main__":
    # Quick test - print one sample response per intent
    for intent in responses:
        print(f"{intent}: {get_response(intent)}")
