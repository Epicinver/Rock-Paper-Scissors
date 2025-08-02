import pyautogui
import time
import random

# Get the list of words
words_input = input("Enter words that shall be typed [separated by commas]: ")
words = [word.strip() for word in words_input.split(",") if word.strip()]

# Get delay between words
try:
    delay = float(input("How long will the delay be after each word (in seconds)? "))
except ValueError:
    print("Invalid delay. Using default of 1 second.")
    delay = 1.0

# Get total duration
try:
    total_duration = float(input("How long should the script run for? (in seconds): "))
except ValueError:
    print("Invalid time. Using default of 10 seconds.")
    total_duration = 10.0

print("Typing will start in 5 seconds... switch to the input window now!")
time.sleep(5)

# Record start time
start_time = time.time()

# Loop until the duration has passed
while (time.time() - start_time) < total_duration:
    word = random.choice(words)
    pyautogui.typewrite(word)
    pyautogui.press('enter')  # Change to ' ' if you want a space instead
    time.sleep(delay)

print("Done!")
