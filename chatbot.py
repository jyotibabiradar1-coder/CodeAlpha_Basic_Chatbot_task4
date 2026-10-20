"""
CodeAlpha Internship - Task 4: Basic Chatbot
Author: Intern
Description: A simple rule-based conversational chatbot built using functions,
             loops, and if-elif branching to match user inputs and return
             predefined responses.
Key Concepts Used: if-elif, functions, loops, input/output.
"""

import datetime
import random

# Predefined jokes collection for interactive banter
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python developer wear glasses? Because they couldn't C#!",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "Why was the JavaScript developer sad? Because they didn't know how to 'null' their feelings.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'"
]


def display_welcome_banner():
    """Prints the introduction banner and instructions."""
    print("\n" + "=" * 55)
    print("           WELCOME TO ALPHABOT (CODEALPHA)")
    print("=" * 55)
    print("Hello! I am AlphaBot, your rule-based virtual assistant.")
    print("Ask me questions, chat with me, or type 'help' for ideas.")
    print("Type 'bye', 'exit', or 'quit' to end our chat.")
    print("=" * 55 + "\n")


def display_help():
    """Returns a formatted string of supported conversation topics."""
    return (
        "Here are some things you can say to me:\n"
        "  - Greetings: 'hello', 'hi', 'hey', 'good morning'\n"
        "  - Well-being: 'how are you', 'how are you doing'\n"
        "  - Identity: 'who are you', 'what is your name'\n"
        "  - Fun: 'tell me a joke'\n"
        "  - Utilities: 'what time is it', 'what is today's date'\n"
        "  - Creator/Internship: 'what is codealpha', 'about internship'\n"
        "  - Ending chat: 'bye', 'goodbye', 'quit'"
    )


def get_bot_response(user_input):
    """
    Evaluates user input string and returns the bot's response using
    if-elif-else conditional logic.
    
    Returns:
        tuple: (response_text, should_exit_flag)
    """
    # Normalize input: lowercase and stripped of outer whitespace
    cleaned_input = user_input.strip().lower()

    # Rule 1: Empty input check
    if not cleaned_input:
        return "You didn't say anything! Feel free to ask me something or type 'help'.", False

    # Rule 2: Farewells / Exit condition
    elif (
        cleaned_input in ("bye", "goodbye", "see you", "exit", "quit", "cya")
        or "bye" in cleaned_input
        or "see you" in cleaned_input
    ):
        return "Goodbye! Have a wonderful day ahead!", True

    # Rule 3: Greetings
    elif (
        cleaned_input in ("hello", "hi", "hey", "hola")
        or cleaned_input.startswith("hello")
        or cleaned_input.startswith("hi ")
        or cleaned_input.startswith("hey")
    ):
        greetings = [
            "Hi! How can I help you today? :)",
            "Hello there! It's great to chat with you!",
            "Hey! What's on your mind today?"
        ]
        return random.choice(greetings), False

    # Rule 4: Time of day greetings
    elif "good morning" in cleaned_input:
        return "Good morning! Wishing you a productive and happy day!", False

    elif "good afternoon" in cleaned_input:
        return "Good afternoon! Hope your day is going smoothly!", False

    elif "good evening" in cleaned_input:
        return "Good evening! How has your day been?", False

    # Rule 5: Inquiries about well-being
    elif (
        "how are you" in cleaned_input
        or "how do you do" in cleaned_input
        or "how's it going" in cleaned_input
        or "how is it going" in cleaned_input
    ):
        return "I'm fine, thanks! Operating at 100% efficiency. How are you doing?", False

    elif "i am fine" in cleaned_input or "i'm good" in cleaned_input or "doing well" in cleaned_input:
        return "Glad to hear that! Keep up the positive energy!", False

    # Rule 6: Name & Identity
    elif (
        "what is your name" in cleaned_input
        or "who are you" in cleaned_input
        or "what are you" in cleaned_input
    ):
        return "I am AlphaBot, a rule-based chatbot built in Python for the CodeAlpha internship!", False

    # Rule 7: CodeAlpha Internship
    elif "codealpha" in cleaned_input or "internship" in cleaned_input:
        return (
            "CodeAlpha provides practical, hands-on software development internships "
            "empowering students to master real-world coding skills!",
            False
        )

    # Rule 8: Asking for Help / Commands
    elif cleaned_input in ("help", "options", "commands", "what can you do"):
        return display_help(), False

    # Rule 9: Time and Date queries
    elif "time" in cleaned_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}.", False

    elif "date" in cleaned_input or "day" in cleaned_input:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}.", False

    # Rule 10: Entertainment / Jokes
    elif "joke" in cleaned_input or "make me laugh" in cleaned_input:
        return random.choice(JOKES), False

    # Rule 11: Gratitude / Courtesy
    elif "thank" in cleaned_input:
        return "You're very welcome! Always happy to assist.", False

    # Rule 12: Default / Fallback response
    else:
        return (
            "I'm sorry, I didn't quite catch that. "
            "Try asking 'how are you', 'tell me a joke', 'what time is it', or type 'help'!",
            False
        )


def chat():
    """Main chatbot conversational loop."""
    display_welcome_banner()

    while True:
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\n\nAlphaBot: Session interrupted. Goodbye!\n")
            break

        bot_reply, should_exit = get_bot_response(user_input)
        print(f"AlphaBot: {bot_reply}\n")

        if should_exit:
            break


def main():
    """Entry point for running the chatbot."""
    chat()


if __name__ == "__main__":
    main()
