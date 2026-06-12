# 🤖 Rule-Based AI Chatbot

A sophisticated, production-quality rule-based chatbot built in **pure Python** — no external ML libraries needed.

## Architecture

```
project1_rule_based_chatbot/
│
├── main.py          ← Entry point (CLI interface with ANSI colours)
├── chatbot.py       ← Core engine: intent detection + response generation
├── responses.py     ← Knowledge base: all response templates
├── context.py       ← Session state tracker (turn count, intent history)
├── test_chatbot.py  ← Full test suite (pytest)
└── requirements.txt ← Only pytest needed
```

## Features

| Feature | Details |
|---|---|
| Intent Detection | 20+ intent categories via compiled regex patterns |
| Context Tracking | Remembers past intents, dominant topic, turn count |
| Math Engine | Evaluates arithmetic expressions inline (`12 * 7`) |
| Live Time/Date | Returns current system time and date |
| Jokes KB | 5 built-in jokes, randomly selected |
| Fallback Logic | Context-aware fallback messages |
| Session Stats | `stats` command shows turn count, session length |
| Test Suite | 20+ unit tests covering intents, responses, context |

## Quick Start

```bash
# Python 3.10+ required
python main.py
```

### Optional: run tests
```bash
pip install pytest
python -m pytest test_chatbot.py -v
```

## Sample Session

```
  You > hello
  🤖 Aria: Hello there! I'm Aria. How can I help you today?

  You > what is 15 * 8
  🤖 Aria: 15 * 8 = 120

  You > tell me a joke
  🤖 Aria: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

  You > stats
  ── Session Stats ──────────────────────
  Turns:          3
  Session length: 0:00:12
  Intents seen:   greeting, math, joke

  You > bye
  🤖 Aria: Goodbye! It was a pleasure chatting. Take care! 👋
```

## Extending the Bot

1. **Add intents** – Drop a new key into `RESPONSES` in `responses.py`  
2. **Add patterns** – Add regex strings to the matching intent in `chatbot.py → _build_intent_patterns()`  
3. **Add computed responses** – Add an `if intent == "new_intent":` block in `generate_response()`
