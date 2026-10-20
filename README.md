# Task 4: Basic Chatbot (Python)

A simple rule-based conversational **Chatbot** built using Python as part of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
AlphaBot is an interactive console chatbot that interprets user queries and responds using predefined rules and conditions. It demonstrates fundamental control flow patterns including conditionals, modular functions, string processing, and loop management.

### Features
- **Conversational Responses**: Responds naturally to greetings (`"hello"`, `"hi"`, `"good morning"`), inquiries (`"how are you"`), gratitude, and farewells (`"bye"`, `"quit"`).
- **Rule-Based Intent Recognition**: Uses cascading `if-elif-else` constructs to match user prompts with appropriate responses.
- **Dynamic Capabilities**:
  - Provides real-time system time and date.
  - Shares programming jokes.
  - Explains the CodeAlpha internship context.
  - Offers a `'help'` command listing recognized topics.
- **Graceful Session Termination**: Closes cleanly upon detecting farewell triggers or keyboard interruptions.

---

## 🛠️ Key Concepts Used
- **`if-elif-else`**: Evaluating intents and selecting predefined replies.
- **Functions**: Structured code separation (`get_bot_response()`, `display_help()`, `chat()`).
- **Loops**: Continuous conversation loop (`while True`).
- **Input/Output**: Formatted interactive CLI dialogue with the user.

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this directory:
   ```bash
   cd Task4_Basic_Chatbot
   ```
3. Run the script:
   ```bash
   python chatbot.py
   ```

---

## 💬 Sample Conversation

```text
=======================================================
           WELCOME TO ALPHABOT (CODEALPHA)
=======================================================
Hello! I am AlphaBot, your rule-based virtual assistant.
Ask me questions, chat with me, or type 'help' for ideas.
Type 'bye', 'exit', or 'quit' to end our chat.
=======================================================

You: hello
AlphaBot: Hi! How can I help you today? 😊

You: how are you
AlphaBot: I'm fine, thanks! Operating at 100% efficiency. How are you doing?

You: tell me a joke
AlphaBot: Why do programmers prefer dark mode? Because light attracts bugs!

You: what time is it
AlphaBot: The current time is 11:35 PM.

You: bye
AlphaBot: Goodbye! Have a wonderful day ahead! 👋
```
