import random

#adam asmaca adımları
pics = [""" 
   +---+
   |   |
       |
       |
       |
       |
=========""","""
   +---+
   |   |
   O   |
       |
       |
       |
=========""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========="""]

while True:
    word = random.choice(["windows", "apple", "bus", "python"]) #örnek kelimeler
    step = 0 #adım sayısını 0'dan başlayacak
    letters = [] 
    
    while True:
        print(pics[step])
        for i, char in enumerate(word):
            print(char if i in letters else "_") #yazılan kelimenin harflerinden birisi varsa yazdırır yoksa da _ yazdırılmaya devam eder.
        answer = input("\nAnswer: ")  
        if answer == word:
            print("You win!\n")
            break
        else:
            while True:
                rand = random.randint(0, len(word))
                if not rand in letters:
                    letters.append(rand)
                    break
            step += 1
        if step >= len(pics):
            print("You lose!\n")
            break
    if not "y" == input("Play again (y/n): "):
        break