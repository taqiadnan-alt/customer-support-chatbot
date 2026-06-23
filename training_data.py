# Training data for our Intent Classifier
# Each intent has multiple example phrases - the model learns the PATTERN across these

training_data = {
    "greeting": [
        "Hi",
        "Hello",
        "Hey there",
        "Good morning",
        "Hey, how are you?",
        "Hey",
        "Good Evening",
        "hi there",
        "hello, is anyone available",
    ],
    "order_status": [
        "Where is my order?",
        "When will my package arrive?",
        "Has my order shipped yet?",
        "I want to track my order",
        "What's the status of my delivery?",
        "where is my order",
        "when will i receive my order",
        "When will I receive my package?",
        "hey, where's my order",
        "hi, when will my package arrive",
    ],
    "refund_request": [
        "I want a refund",
        "Can I get my money back?",
        "How do I return this product?",
        "I'd like to cancel and get refunded",
        "This isn't what I ordered, refund please",
        "I need a refund for this item as this item is damaged",
        "this is broken, I want my money back",
        "I want to return this and get my money back",
    ],
    "complaint": [
        "This product is broken",
        "I'm very unhappy with my purchase",
        "The item I received is damaged",
        "This is the worst service ever",
        "My order arrived in bad condition",
        "the item is damaged",
        "I received a wrong item",
        "I need to replace it",
        "where's my stuff, this is taking forever",
        "I'm so disappointed with this purchase",
    ],
    "shipping_time": [
        "How long does shipping take?",
        "What are your delivery times?",
        "How fast can I get my order?",
        "Do you offer express shipping?",
        "When can I expect delivery?",
        "what time will I receive order?",
        "At what time the item will be delivered?",
        "What will be the shipping time of the ordered item?",
    ],
    "goodbye": [
        "Bye",
        "Thanks, that's all",
        "See you later",
        "That's all I needed, thank you",
        "Goodbye",
        "Ok thank you bye",
        "No that's everything",
        "Thanks buddy!!!",
        "Ok, Catch you next time!!",
    ],
    "fallback": [
        "What's the weather today?",
        "Tell me a joke",
        "Can you sing a song?",
        "What is your favorite color?",
        "asdkjaskjd random text",
        "do you like pizza",
        "what's 2 plus 2",
        "What's around the world happening?",
        "any movie suggestion",
    ],
    "cancel_order": [
        "I wanna cancel my order as I'll not be available on the particular delivery date.",
        "I want to cancel the item I ordered as the item is available in the nearby offline store as I want the item early asap!!",
        "Please cancel my order",
        "Can I cancel my order before it ships?",
        "I changed my mind, I don't want this order anymore",
        "How do I cancel my purchase?",
        "I don't want this order anymore, please stop it",
        "can you stop my order before it ships",
        "cancel order number 12345",
        "I'd like to cancel my purchase, it hasn't shipped yet",
    ],
    "payment_issue": [
        "I made the payment but I didn't receive the confirmation order mail or sms.",
        "The amount of the item I ordered is showing the wrong amount in the payment section",
        "My payment failed but money got deducted from my account",
        "I was charged twice for the same order",
        "My card got declined while paying",
        "The payment page is not accepting my card",
    ],
    "product_availability": [
        "I would like to confirm whether the particular item is available or not?",
        "For the particular item is there more colour options or not?",
        "Size 9 is available for this item?",
        "Is this product in stock?",
        "When will this item be back in stock?",
        "Do you have this in a different size?",
        "do you have this in blue",
        "is this available in other colors",
        "does this come in medium",
        "is this still in stock",
    ],
}

if __name__ == "__main__":
    total = sum(len(v) for v in training_data.values())
    print(f"Total intents: {len(training_data)}")
    print(f"Total examples: {total}")
    for intent, examples in training_data.items():
        print(f"\n{intent} ({len(examples)} examples):")
        for ex in examples:
            print(f"  - {ex}")
