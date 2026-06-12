"""
context.py  –  Conversation state tracker.
Keeps track of the current session's turns, intents, and timing.
"""

from datetime import datetime
from collections import Counter
from typing import Optional


class ConversationContext:
    """
    Lightweight session-scoped context that stores:
    - Full conversation history (input + detected intent)
    - Rolling intent history for context-aware replies
    - Turn count & session timing
    """

    MAX_HISTORY = 50  # cap memory to last N turns

    def __init__(self):
        self.reset()

    def reset(self):
        """Start a fresh session."""
        self.history: list[dict] = []
        self.intent_history: list[str] = []
        self.turn_count: int = 0
        self.session_start: datetime = datetime.now()
        self.last_intent: Optional[str] = None

    def add_turn(self, user_input: str, intent: str):
        """Record a new conversation turn."""
        self.history.append({
            "turn": self.turn_count + 1,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "user": user_input,
            "intent": intent,
        })
        # Trim to cap
        if len(self.history) > self.MAX_HISTORY:
            self.history = self.history[-self.MAX_HISTORY:]

        self.intent_history.append(intent)
        self.last_intent = intent
        self.turn_count += 1

    @property
    def dominant_intent(self) -> Optional[str]:
        """Return the most common intent this session (excluding 'unknown')."""
        filtered = [i for i in self.intent_history if i != "unknown"]
        if not filtered:
            return None
        return Counter(filtered).most_common(1)[0][0]

    def summary(self) -> dict:
        """Snapshot of the current session state."""
        return {
            "turns": self.turn_count,
            "dominant_intent": self.dominant_intent,
            "last_intent": self.last_intent,
            "session_duration_s": (datetime.now() - self.session_start).seconds,
        }
