"""
Rule-Based AI Chatbot
=====================
A sophisticated rule-based chatbot using pattern matching, intent detection,
context tracking, and a rich knowledge base.
"""

from distro import name
import sympy as sp
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr
import math

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

        # Memory
        self.memory = {}

        self._build_intent_patterns()

    # ------------------------------------------------------------------
    # Pattern compilation
    # ------------------------------------------------------------------

    def _build_intent_patterns(self):
        """Compile all regex patterns once at startup for speed."""
        self.patterns = {
            intent: [re.compile(p, re.IGNORECASE) for p in patterns]
            for intent, patterns in {
                "greeting": [
                    r"\b(hi|hello|hey|howdy|sup|good\s+(morning|afternoon|evening|day))\b"
                ],
                "farewell": [
                    r"\b(bye|goodbye|exit|quit|see\s+you|later|cya|take\s+care|farewell)\b"
                ],
                "thanks": [r"\b(thank(s| you)|thx|ty|appreciate)\b"],
                "help": [r"\b(help|assist|support|what can you do|commands|options)\b"],
                "name_query": [
                    r"\b(what('?s| is)? your name|your name|ur name|what is ur name|who are you|what are you called|what should i call you)\b"
                ],
                "creator_query": [
                    r"\b(who made you|who built you|who created you|who made u|your creator|your developer)\b"
                ],
                "time_query": [r"\b(what time|current time|time now)\b"],
                "date_query": [r"\b(what (day|date)|today's date|current date)\b"],
                "weather_query": [
                    r"\b(weather|temperature|forecast|rain|sunny|cloudy)\b"
                ],
                "joke": [
                    r"\b(joke|funny|one more|tell me one more|make me laugh|humor|tell me something funny)\b"
                ],
                "feeling": [
                    r"\b(how are you|how are u|how are u doing do you feel|are you okay|you good)\b"
                ],
                "about": [
                    r"\b(about you|tell me about yourself|tell me about ur self|tell me about u||describe yourself|what are you)\b"
                ],
                "age_query": [
                    r"\b(how old are you|how old are u|your age|ur age|when were you (born|created)|when were u (born|created))\b"
                ],
                "capable_query": [
                    r"\b(what can you (do|help)|what can u (do|help)|your (skills|capabilities|features)|ur (skills|capabilities|features))\b"
                ],
                "math": [
                    r"[\d\+\-\*\/\(\)\^\.\%]+",
                    r"\b(solve|integrate|differentiate|sqrt|sin|cos|tan|log|factorial)\b",
                ],
                "affirmation": [
                    r"\b(yes|yeah|yep|yup|sure|ok|okay|alright|absolutely|definitely)\b"
                ],
                "negation": [r"\b(no|nope|nah|not really|i don't think so|negative)\b"],
                "compliment": [
                    r"\b(good (bot|job|work)|you('re| are) (great|awesome|amazing|cool|smart))\b"
                ],
                "insult": [r"\b(stupid|dumb|useless|hate you|idiot|terrible|awful)\b"],
                "remember_name": [r"my name is (\w+)"],
                "ask_name": [r"\b(what is my name|who am i|do you remember my name)\b"],
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
        name_match = re.search(r"my name is (\w+)", user_input, re.IGNORECASE)

        if name_match:
            name = name_match.group(1)

            self.memory["user_name"] = name

            return f"Nice to meet you, {name}! I'll remember your name."

        self.context.add_turn(user_input, intent)

        # --- special computed intents ---
        if intent == "farewell":
            self.context.reset()
            return random.choice(self.responses["farewell"]).format(name=self.name)

        if intent == "math":
            return self._handle_math(user_input)

        if intent == "time_query":
            return f"The current time is {datetime.now().strftime('%I:%M %p')}."
        if re.search(
            r"what is my name|who am i|do you remember my name",
            user_input,
            re.IGNORECASE,
        ):
            if "user_name" in self.memory:
                return f"Your name is {self.memory['user_name']}."

            return "I don't know your name yet. Tell me by saying 'My name is ...'"

        if intent == "date_query":
            return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

        # --- standard intent lookup ---
        if intent in self.responses:
            template = random.choice(self.responses[intent])
            return template.format(name=self.name)

        # --- context-aware fallback ---
        if intent == "unknown":
            return random.choice(
                [
                    "I'm not sure I understood that.",
                    "Could you rephrase your question?",
                    "I don't have an answer for that yet.",
                    "Try asking something else.",
                    "Sorry, I couldn't understand that.",
                ]
            )

        return random.choice(self.fallbacks)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _handle_math(self, text: str) -> str:
        try:
            text = text.lower().strip()

            x = symbols("x")

            if text.startswith("solve"):
                equation = text.replace("solve", "").strip()

                if "=" not in equation:
                    return "Please provide an equation. " "Example: solve x+5=10"

                left, right = equation.split("=")

                eq = sp.Eq(parse_expr(left), parse_expr(right))

                solution = sp.solve(eq, x)

                return f"Solution: {solution}"

            # -------------------------
            # Differentiate
            # -------------------------
            if text.startswith("differentiate"):
                expr = text.replace("differentiate", "").strip()

                derivative = sp.diff(parse_expr(expr), x)

                return f"Derivative: {derivative}"

            # -------------------------
            # Integrate
            # -------------------------
            if text.startswith("integrate"):
                expr = text.replace("integrate", "").strip()

                integral = sp.integrate(parse_expr(expr), x)

                return f"Integral: {integral} + C"

            # -------------------------
            # Simplify
            # -------------------------
            if text.startswith("simplify"):
                expr = text.replace("simplify", "").strip()

                return f"Simplified: " f"{sp.simplify(parse_expr(expr))}"

            # -------------------------
            # Expand
            # -------------------------
            if text.startswith("expand"):
                expr = text.replace("expand", "").strip()

                return f"Expanded: " f"{sp.expand(parse_expr(expr))}"

            # -------------------------
            # Factor
            # -------------------------
            if text.startswith("factor"):
                expr = text.replace("factor", "").strip()

                return f"Factored: " f"{sp.factor(parse_expr(expr))}"

            # -------------------------
            # Factorial Notation
            # -------------------------
            factorial_match = re.match(r"(\d+)!", text)

            if factorial_match:
                n = int(factorial_match.group(1))

                return f"{n}! = " f"{math.factorial(n)}"

            # -------------------------
            # Power Support
            # -------------------------
            text = text.replace("^", "**")

            allowed = {
                "sqrt": sp.sqrt,
                "sin": lambda v: sp.sin(v * sp.pi / 180),
                "cos": lambda v: sp.cos(v * sp.pi / 180),
                "tan": lambda v: sp.tan(v * sp.pi / 180),
                "log": sp.log,
                "log10": lambda v: sp.log(v, 10),
                "factorial": sp.factorial,
                "pi": sp.pi,
                "e": sp.E,
            }

            result = eval(text, {"__builtins__": None}, allowed)

            return f"Result = {float(sp.N(result)):.2f}"

        except Exception as e:
            return f"Math Error: " f"{str(e)}"

    def get_stats(self) -> dict:
        """Return session statistics."""
        return {
            "total_turns": self.context.turn_count,
            "intents_seen": list(self.context.intent_history),
            "session_length": str(datetime.now() - self.context.session_start).split(
                "."
            )[0],
        }
