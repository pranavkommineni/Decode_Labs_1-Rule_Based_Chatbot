#  Rule-Based AI Chatbot

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

## Daily Work Log – Rule-Based AI Chatbot

--- 
## [02/06/2025]

### Project Planning & Requirement Analysis

- Analyzed the project requirements for a rule-based AI chatbot.
- Designed the overall chatbot architecture and folder structure.

### Identified major components:
- Intent Detection Module
- Response Management System
- Context Tracking Module
- Command Line Interface (CLI)
- Testing Framework
- Prepared development environment and project dependencies.
- Deliverables
- Initial project structure.
- Architecture planning.
- Dependency setup.
---
---
## [03/06/2025]

### Core Chatbot Engine Development

- Developed the main chatbot engine in Python.
- Implemented regex-based intent classification.
  
### Created support for multiple conversational intents:
- Greetings
- Farewells
- Thanks
- Help Requests
- Name Queries
- Creator Queries
- Time Queries
- Date Queries
- Weather Queries
- Jokes
- Feelings
- About Bot
- Age Queries
- Capability Queries
- Compliments
- Insults
- Affirmations
- Negations
- Optimized intent matching using compiled regular expressions.
- Deliverables
`chatbot.py completed.`
#### Intent detection system implemented.
---
---
## [04/06/2025]

### Knowledge Base & Context Management
- Developed response management module.
- Created structured response templates for all supported intents.
- Implemented fallback response handling for unknown queries.
- Developed conversation context tracker.

### Added:
- Conversation history storage
- Intent history tracking
- Session statistics tracking
- Dominant intent analysis
- Turn count monitoring
- Implemented session reset functionality.
- Deliverables

`responses.py completed.`
`context.py completed.`
`Multi-turn conversation support added.`
---
---
## [05/06/2025]

### User Interface, Testing & Documentation
- Developed interactive Command Line Interface (CLI).
- Added colored terminal output for improved user experience.
### Implemented:
- Session statistics command
- Graceful exit handling
- Interactive user prompts
- Developed comprehensive test suite using PyTest.
### Tested:
- Intent classification
- Response generation
- Mathematical operations
- Context management
- Session statistics
- Created project documentation and usage guide.
- Deliverables
`main.py completed.`
`test_chatbot.py completed.`
- README documentation prepared.
---
---
## Key Features Implemented
- Intent Detection
- 20+ intent categories supported.
- Regex-based pattern matching.
- Fast compiled pattern execution.
- Conversation Management
- Session memory.
- Intent history tracking.
- Dominant intent identification.
- Conversation statistics.
- Utility Functions
- Mathematical expression evaluation.
- Current date retrieval.
- Current time retrieval.
- User Experience
- Interactive CLI interface.
- Colored terminal responses.
- Session analytics dashboard.
---

### Testing
- Automated unit tests using PyTest.
- Validation of chatbot responses.
- Context management verification.
- Intent detection accuracy testing.
---

### Technologies Used
- Python 3
- Regular Expressions (Regex)
- PyTest
- Object-Oriented Programming (OOP)
- Command Line Interface (CLI)
---