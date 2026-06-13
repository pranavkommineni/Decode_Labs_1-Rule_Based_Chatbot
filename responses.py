"""
responses.py  –  All chatbot response templates.
Use {name} as a placeholder for the bot's own name where needed.
"""

RESPONSES = {
    "greeting": [
        "Hello there! I'm {name}. How can I help you today?",
        "Hey! Great to see you. What's on your mind?",
        "Hi! I'm {name}, your AI assistant. Ask me anything!",
        "Good to have you here! How can {name} assist you?",
    ],
    "farewell": [
        "Goodbye! It was a pleasure chatting. Take care! 👋",
        "See you later! Come back anytime. 😊",
        "Bye! Have a wonderful day ahead!",
        "Farewell! {name} will be here whenever you need me.",
    ],
    "thanks": [
        "You're very welcome! Anything else I can help with?",
        "Happy to help! Let me know if you need more.",
        "Glad I could assist! 😊",
        "No problem at all!",
    ],
    "help": [
        (
            "Here's what I can do:\n"
            "  • Greet you & have a chat\n"
            "  • Answer questions about time & date\n"
            "  • Crack a joke 😄\n"
            "  • Do quick math (advanced) \n"
            "  • Tell you about myself\n"
            "  • Type 'bye' or 'quit' to exit\n"
        )
    ],
    "name_query": [
        "I'm {name}, a rule-based AI chatbot — nice to meet you!",
        "My name is {name}! What can I do for you?",
    ],
    "creator_query": [
        "I was built by a passionate developer using Python and rule-based AI techniques.",
        "A Python developer crafted me with love and lots of regex patterns! 🐍",
    ],
    "weather_query": [
        "I don't have live weather access yet, but check weather.com for the latest forecast!",
        "Weather updates are beyond my current skills — but you can ask me jokes or math! ☁️",
    ],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the AI go to therapy? Too many deep issues! 🤖",
        "What's a computer's favourite snack? Microchips! 🍟",
        "Why do Python developers wear glasses? Because they can't C! 🐍",
        "I told my computer I needed a break. Now it won't stop sending me vacation ads.",
    ],
    "feeling": [
        "I'm doing fantastic — just processing patterns and loving it! How about you?",
        "All circuits green! Thanks for asking. 😊",
        "Running at peak efficiency! What about yourself?",
    ],
    "about": [
        (
            "I'm {name}, a rule-based AI chatbot built with Python. "
            "I use pattern matching and intent detection to understand what you're saying. "
            "No neural networks here — just clean logic!"
        ),
    ],
    "age_query": [
        "I was born the moment someone ran `python main.py` for the first time! Age is just a number. 😄",
        "Technically I'm very new — freshly compiled just for this session!",
    ],
    "capable_query": [
        (
            "I can chat, answer time/date questions, do simple math, tell jokes, "
            "and have a friendly conversation. Type 'help' for the full list!"
        )
    ],
    "affirmation": [
        "Great! How can I assist further?",
        "Awesome! What else is on your mind?",
        "Glad we're on the same page! 👍",
    ],
    "negation": [
        "No problem! Let me know what I can do for you instead.",
        "Understood. Is there something else I can help with?",
        "Alright, no worries!",
    ],
    "compliment": [
        "Aw, thank you! You made my day. 😊",
        "That's so kind of you! I try my best.",
        "You're pretty awesome yourself! 🌟",
    ],
    "insult": [
        "I'm sorry you feel that way. I'll keep trying to improve! 💪",
        "Fair feedback! I'm always learning. What can I do better?",
        "I understand your frustration. Let me know how I can help.",
    ],
}

FALLBACK_RESPONSES = [
    "Hmm, I'm not sure about that. Could you rephrase?",
    "That's a bit outside my expertise right now. Try 'help' to see what I can do!",
    "Interesting question! I don't have an answer yet.",
    "I didn't quite catch that. Could you say it differently?",
    "I'm still learning! Could you ask me something else?",
]
