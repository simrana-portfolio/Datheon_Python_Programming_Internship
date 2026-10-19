
import re

# Chatbot responses
responses = {
    "greeting": "Hello! Welcome to Customer Support. How can I help you?",
    "hours": "Our business hours are Monday to Friday, 9:00 AM to 5:00 PM.",
    "price": "Our product prices depend on the selected product. Please tell me which product you are interested in.",
    "delivery": "Delivery usually takes 3 to 5 business days.",
    "return": "You can return eligible products within 7 days of purchase.",
    "contact": "You can contact our support team at support@example.com.",
    "thanks": "You're welcome! Happy to help.",
    "fallback": "Sorry, I didn't understand that. Please ask about business hours, prices, delivery, returns, or contact details."
}

# Keywords and regular expressions
intents = {
    "greeting": r"\b(hello|hi|hey|good morning|good afternoon)\b",
    "hours": r"\b(hours|opening|closing|open|close|working time)\b",
    "price": r"\b(price|cost|product|products|how much)\b",
    "delivery": r"\b(delivery|shipping|arrive|tracking)\b",
    "return": r"\b(return|refund|exchange)\b",
    "contact": r"\b(contact|email|phone|support)\b",
    "thanks": r"\b(thanks|thank you|thank)\b"
}

def chatbot():
    print("======================================")
    print("       CUSTOMER SUPPORT CHATBOT")
    print("======================================")
    print("Bot: Hello! Welcome to Customer Support.")
    print("Bot: Type 'bye', 'exit', or 'quit' to end.")

    while True:
        user_input = input("\nYou: ").strip().lower()

        if not user_input:
            print("Bot: Please enter a message.")
            continue

        # Check exit commands
        if re.fullmatch(r"(bye|exit|quit)", user_input):
            print("Bot: Thank you for contacting us. Goodbye!")
            break

        # Identify user intent
        found_intent = None

        for intent, pattern in intents.items():
            if re.search(pattern, user_input):
                found_intent = intent
                break

        # Generate response
        if found_intent:
            print("Bot:", responses[found_intent])
        else:
            print("Bot:", responses["fallback"])


if __name__ == "__main__":
    chatbot()
