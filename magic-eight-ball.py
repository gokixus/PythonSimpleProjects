import random

answers = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no"]

input("Ask your question to magic eight ball: ")
print(f"Answer: {random.choice(answers)}")