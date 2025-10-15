import time
import random

def typing_speed_game():
    print("\n⌨️ Welcome to the Typing Speed Game!")
    print("You'll be shown a random sentence. Type it exactly as fast as you can.\n")
    time.sleep(1)

    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python makes programming fun and easy.",
        "Typing fast requires focus and accuracy.",
        "Never stop learning new things every day.",
        "Code is like humor; it’s better when it works."
    ]

    sentence = random.choice(sentences)
    print("Your sentence:\n")
    print(f"👉 {sentence}\n")
    input("Press Enter when you're ready to start typing... ")

    # Start timing
    start_time = time.time()
    user_input = input("\nType here: ")
    end_time = time.time()

    # Calculate time and accuracy
    total_time = round(end_time - start_time, 2)
    words = len(sentence.split())
    speed = round((words / total_time) * 60, 2)  # Words per minute (WPM)

    # Accuracy check
    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(sentence) and c == sentence[i])
    accuracy = round((correct_chars / len(sentence)) * 100, 2)

    print("\n--- Results ---")
    print(f"Time Taken: {total_time} seconds")
    print(f"Speed: {speed} words per minute")
    print(f"Accuracy: {accuracy}%")

    if accuracy == 100:
        print("🔥 Perfect typing!")
    elif accuracy > 80:
        print("💪 Great job!")
    elif accuracy > 50:
        print("🙂 Not bad, keep practicing!")
    else:
        print("😅 Try again for better accuracy!")

# --- Run Game ---
if __name__ == "__main__":
    typing_speed_game()
