import time
import random

# Random paragraphs list
paragraphs = [
    "Artificial intelligence is transforming industries through automation and deep learning.",
    "Cybersecurity ensures protection against data breaches and malicious attacks worldwide.",
    "Cloud computing provides scalable solutions for businesses and remote collaboration.",
    "Quantum computing pushes the boundaries of processing power beyond imagination."
]

# Select a random paragraph
selected_paragraph = random.choice(paragraphs)

print("\n💡 Type the following paragraph exactly as shown:\n")
print(selected_paragraph)
print("\n")

# Start timing
start_time = time.time()

# User input
user_input = input("👉 Start typing here: ")

# End timing
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time

# Split words for comparison
original_words = selected_paragraph.split()
user_words = user_input.split()

# Count correct words
correct_count = sum(1 for i in range(min(len(original_words), len(user_words))) if original_words[i] == user_words[i])

# Calculate accuracy
total_words = len(original_words)
accuracy = (correct_count / total_words) * 100

# Calculate typing speed (WPM - Words Per Minute)
words_per_minute = (len(user_words) / time_taken) * 60

# Output results
print("\n📊 Typing Speed & Accuracy Report:")
print(f"✅ Total Words in Paragraph: {total_words}")
print(f"✔️ Correct Words Typed: {correct_count}")
print(f"❌ Incorrect Words: {total_words - correct_count}")
print(f"🎯 Accuracy: {accuracy:.2f}%")
print(f"⌛ Time Taken: {time_taken:.2f} seconds")
print(f"⚡ Typing Speed: {words_per_minute:.2f} WPM (Words Per Minute)")
