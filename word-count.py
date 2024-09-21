def wordCount(text):
    count = 0
    words = text.split(" ")
    for word in words:
        if word.isalnum() or word.isalpha():
            count += 1
    return count

text = input("Text: ")
print(f"Total words: {wordCount(text)}") 