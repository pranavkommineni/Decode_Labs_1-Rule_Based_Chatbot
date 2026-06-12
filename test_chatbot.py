"""
test_chatbot.py  –  Unit tests for the Rule-Based AI Chatbot.

Run:
    python -m pytest test_chatbot.py -v
"""

import pytest
from chatbot import RuleBasedChatbot
from context import ConversationContext


@pytest.fixture
def bot():
    return RuleBasedChatbot(bot_name="TestBot")


# ── Intent detection ─────────────────────────────────────────────────

class TestIntentDetection:
    def test_greeting(self, bot):
        assert bot.detect_intent("hello there") == "greeting"
        assert bot.detect_intent("Hey!") == "greeting"
        assert bot.detect_intent("Good morning") == "greeting"

    def test_farewell(self, bot):
        assert bot.detect_intent("bye") == "farewell"
        assert bot.detect_intent("goodbye friend") == "farewell"
        assert bot.detect_intent("see you later") == "farewell"

    def test_thanks(self, bot):
        assert bot.detect_intent("thank you") == "thanks"
        assert bot.detect_intent("thanks!") == "thanks"

    def test_joke(self, bot):
        assert bot.detect_intent("tell me a joke") == "joke"

    def test_time_query(self, bot):
        assert bot.detect_intent("what time is it") == "time_query"

    def test_date_query(self, bot):
        assert bot.detect_intent("what is today's date") == "date_query"

    def test_math(self, bot):
        assert bot.detect_intent("12 + 7") == "math"
        assert bot.detect_intent("what is 100 * 3") == "math"

    def test_unknown(self, bot):
        assert bot.detect_intent("xyzzy plugh twisty") == "unknown"


# ── Response generation ──────────────────────────────────────────────

class TestResponseGeneration:
    def test_greeting_response(self, bot):
        resp = bot.generate_response("hello")
        assert isinstance(resp, str) and len(resp) > 0

    def test_math_addition(self, bot):
        resp = bot.generate_response("5 + 3")
        assert "8" in resp

    def test_math_multiplication(self, bot):
        resp = bot.generate_response("6 * 7")
        assert "42" in resp

    def test_division_by_zero(self, bot):
        resp = bot.generate_response("10 / 0")
        assert "zero" in resp.lower()

    def test_time_response_contains_colon(self, bot):
        resp = bot.generate_response("what time is it?")
        assert ":" in resp  # time format HH:MM

    def test_date_response_not_empty(self, bot):
        resp = bot.generate_response("what is today's date?")
        assert len(resp) > 5

    def test_empty_input(self, bot):
        resp = bot.generate_response("")
        assert "type" in resp.lower() or "something" in resp.lower()

    def test_farewell_resets_context(self, bot):
        bot.generate_response("hello")
        bot.generate_response("bye")
        assert bot.context.turn_count == 0


# ── Context tracking ─────────────────────────────────────────────────

class TestConversationContext:
    def test_turn_count_increments(self, bot):
        bot.generate_response("hi")
        bot.generate_response("how are you")
        assert bot.context.turn_count == 2

    def test_last_intent_updates(self, bot):
        bot.generate_response("hi")
        assert bot.context.last_intent == "greeting"

    def test_reset_clears_state(self):
        ctx = ConversationContext()
        ctx.add_turn("hello", "greeting")
        ctx.reset()
        assert ctx.turn_count == 0
        assert ctx.last_intent is None

    def test_dominant_intent(self):
        ctx = ConversationContext()
        for _ in range(3):
            ctx.add_turn("hi", "greeting")
        ctx.add_turn("bye", "farewell")
        assert ctx.dominant_intent == "greeting"


# ── Stats ────────────────────────────────────────────────────────────

class TestStats:
    def test_stats_keys(self, bot):
        bot.generate_response("hello")
        stats = bot.get_stats()
        assert "total_turns" in stats
        assert "intents_seen" in stats
        assert "session_length" in stats
