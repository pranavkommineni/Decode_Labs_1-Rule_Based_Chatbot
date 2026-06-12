"""
Rule-Based AI Chatbot
=====================
A sophisticated rule-based chatbot using pattern matching, intent detection,
context tracking, and a rich knowledge base.
"""

import re
import random
import json
from datetime import datetime
from typing import Optional
from responses import RESPONSES, FALLBACK_RESPONSES
from context import ConversationContext


class RuleBasedChatbot:
    """
    A rule-based chatbot with:
    - Intent classification via regex patterns
    - Multi-turn context tracking
    - Sentiment-aware responses
    - Pluggable knowledge base
    """

    def __init__(self, bot_name: str = "Aria"):
        self.name = bot_name
        self.context = ConversationContext()
        self.responses = RESPONSES
        self.fallbacks = FALLBACK_RESPONSES
        self._build_intent_patterns()

    # ------------------------------------------------------------------
    # Pattern compilation
    # ------------------------------------------------------------------

    def _build_intent_patterns(self):
        """Compile all regex patterns once at startup for speed."""
        self.patterns = {
            intent: [re.compile(p, re.IGNORECASE) for p in patterns]
            for intent, patterns in {
                "greeting":      [r"\b(hi|hello|hey|howdy|sup|good\s+(morning|afternoon|evening|day))\b"],
                "farewell":      [r"\b(bye|goodbye|exit|quit|see\s+you|later|cya|take\s+care|farewell)\b"],
                "thanks":        [r"\b(thank(s| you)|thx|ty|appreciate)\b"],
                "help":          [r"\b(help|assist|support|what can you do|commands|options)\b"],
                "name_query":    [r"\b(your name|who are you|what are you called|what should i call you)\b"],
                "creator_query": [r"\b(who made you|who built you|who created you|your creator|your developer)\b"],
                "time_query":    [r"\b(what time|current time|time now)\b"],
                "date_query":    [r"\b(what (day|date)|today's date|current date)\b"],
                "weather_query": [r"\b(weather|temperature|forecast|rain|sunny|cloudy)\b"],
                "joke":          [r"\b(joke|funny|make me laugh|humor|tell me something funny)\b"],
                "feeling":       [r"\b(how are you|how do you feel|are you okay|you good)\b"],
                "about":         [r"\b(about you|tell me about yourself|describe yourself|what are you)\b"],
                "age_query":     [r"\b(how old are you|your age|when were you (born|created))\b"],
                "capable_query": [r"\b(what can you (do|help)|your (skills|capabilities|features))\b"],
                "math":          [r"(\d+)\s*([\+\-\*\/\%])\s*(\d+)"],
                "affirmation":   [r"\b(yes|yeah|yep|yup|sure|ok|okay|alright|absolutely|definitely)\b"],
                "negation":      [r"\b(no|nope|nah|not really|i don't think so|negative)\b"],
                "compliment":    [r"\b(good (bot|job|work)|you('re| are) (great|awesome|amazing|cool|smart))\b"],
                "insult":        [r"\b(stupid|dumb|useless|hate you|idiot|terrible|awful)\b"],
            }.items()
        }

    # ------------------------------------------------------------------
    # Intent detection
    # ------------------------------------------------------------------

    def detect_intent(self, user_input: str) -> str:
        """Return the best-matching intent for a user message."""
        for intent, compiled_patterns in self.patterns.items():
            for pattern in compiled_patterns:
                if pattern.search(user_input):
                    return intent
        return "unknown"

    # ------------------------------------------------------------------
    # Response generation
    # ------------------------------------------------------------------

    def generate_response(self, user_input: str) -> str:
        """Main response pipeline."""
        user_input = user_input.strip()
        if not user_input:
            return "Please type something — I'm listening!"

        intent = self.detect_intent(user_input)
        self.context.add_turn(user_input, intent)

        # --- special computed intents ---
        if intent == "farewell":
            self.context.reset()
            return random.choice(self.responses["farewell"]).format(name=self.name)

        if intent == "math":
            return self._handle_math(user_input)

        if intent == "time_query":
            return f"The current time is {datetime.now().strftime('%I:%M %p')}."

        if intent == "date_query":
            return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

        # --- standard intent lookup ---
        if intent in self.responses:
            template = random.choice(self.responses[intent])
            return template.format(name=self.name)

        # --- context-aware fallback ---
        if self.context.last_intent and self.context.last_intent != "unknown":
            return f"I'm not sure I understood that. Could you rephrase? (Last topic: {self.context.last_intent})"

        return random.choice(self.fallbacks)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _handle_math(self, text: str) -> str:
        """Evaluate simple arithmetic expressions."""
        match = self.patterns["math"][0].search(text)
        if match:
            a, op, b = int(match.group(1)), match.group(2), int(match.group(3))
            try:
                result = eval(f"{a}{op}{b}")  # safe — only digits + operator
                return f"{a} {op} {b} = {result}"
            except ZeroDivisionError:
                return "Division by zero is undefined."
        return "I couldn't parse that expression."

    def get_stats(self) -> dict:
        """Return session statistics."""
        return {
            "total_turns":    self.context.turn_count,
            "intents_seen":   list(self.context.intent_history),
            "session_length": str(datetime.now() - self.context.session_start).split(".")[0],
        }
