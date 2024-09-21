def vowelsCount(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

text = input("Text: ")
print(f"Vowels in text: {vowelsCount(text)}")