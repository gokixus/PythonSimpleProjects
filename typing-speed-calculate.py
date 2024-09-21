import datetime

before = datetime.datetime.now()

text = "Say hello to my little friend."
print(f"Please type: {text}")
userInput = input(": ")

if text == userInput:
    after = datetime.datetime.now()
    timeTaken = after-before
    seconds = timeTaken.total_seconds()
    letter_per_second = round(len(text) / seconds, 1)
    
    print("Correct! You typed at...")
    print(f"Speed: {seconds:.2f} seconds.")
    print(f"Typing Speed: {letter_per_second} letters per second.")
else:
    print("You failed. Try again!")