"""
main.py  –  Entry point for the Rule-Based AI Chatbot.

Run:
    python main.py
"""

import sys
from chatbot import RuleBasedChatbot


# ── ANSI colour helpers ──────────────────────────────────────────────
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    CYAN   = "\033[96m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    GREY   = "\033[90m"
    BLUE   = "\033[94m"


def banner(bot_name: str):
    print(f"""
{C.CYAN}{C.BOLD}
  ╔══════════════════════════════════════════╗
  ║       Rule-Based AI Chatbot  🤖          ║
  ║       Bot: {bot_name:<30}║
  ╚══════════════════════════════════════════╝
{C.RESET}
  {C.GREY}Type 'help' to see capabilities.
  Type 'stats' to view session statistics.
  Type 'bye' or 'quit' to exit.{C.RESET}
""")


def print_bot(msg: str):
    print(f"  {C.CYAN}{C.BOLD}🤖 Aria:{C.RESET} {msg}\n")


def print_user_prompt():
    return input(f"  {C.GREEN}{C.BOLD}You >{C.RESET} ").strip()


def print_stats(bot: RuleBasedChatbot):
    stats = bot.get_stats()
    print(f"\n  {C.YELLOW}── Session Stats ──────────────────────{C.RESET}")
    print(f"  Turns:          {stats['total_turns']}")
    print(f"  Session length: {stats['session_length']}")
    print(f"  Intents seen:   {', '.join(stats['intents_seen']) or 'none'}\n")


# ── Main loop ────────────────────────────────────────────────────────

def main():
    bot = RuleBasedChatbot(bot_name="Aria")
    banner(bot.name)
    print_bot("Hello! I'm Aria, your rule-based AI assistant. How can I help you today?")

    while True:
        try:
            user_input = print_user_prompt()
        except (KeyboardInterrupt, EOFError):
            print_bot("Session interrupted. Goodbye! 👋")
            sys.exit(0)

        if not user_input:
            continue

        # Local CLI commands
        if user_input.lower() == "stats":
            print_stats(bot)
            continue

        response = bot.generate_response(user_input)
        print_bot(response)

        # Exit after farewell response
        intent = bot.context.last_intent
        if intent == "farewell":
            break


if __name__ == "__main__":
    main()
