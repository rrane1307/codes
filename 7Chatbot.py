import re

rules = [
(
r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b",
[
"Hello! How can I help you?",
"Hi! Nice to meet you. How can I assist you?",
"Hello! What would you like to know?"
]
),
(
r"\b(how are you|how r u|how are u)\b",
[

"I am doing well. Thank you for asking!",
"I am fine and ready to help you."
]
),
(
r"\b(what is your name|who are you|your name)\b",
[
"I am a simple rule-based chatbot.",
"I am a chatbot created using predefined rules and pattern matching."
]
),
(
r"\b(help|help me|can you help)\b",
[
"Sure! I can answer simple predefined questions.",
"Of course! Tell me what you would like to know."
]
),
(
r"\b(thank you|thanks|thankyou)\b",
[
"You are welcome!",
"My pleasure!"
]
),
(
r"\b(bye|goodbye|see you|exit|quit)\b",
[
"Goodbye! Have a great day!",
"Bye! It was nice talking to you."
]
)
]

capability_responses = [
"I can respond to greetings, simple questions, thanks, and goodbye messages.",
"I use predefined rules and pattern matching to generate my responses."
]

def normalize_text(text):
    text = text.lower()
    text = text.strip()
    return text
def get_response(user_input):
    message = normalize_text(user_input)
    for pattern, responses in rules:
        if re.search(pattern, message, re.IGNORECASE):
            return responses[0]
    return "Sorry, I do not understand that yet. Please try a simple question."

def chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot.")
    print("Chatbot: Type 'bye' or 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        normalized_input = normalize_text(user_input)
        if normalized_input in {"bye", "goodbye", "exit", "quit"}:
            print("Chatbot:", get_response(user_input))
            break
        response = get_response(user_input)
        print("Chatbot:", response)
chatbot()