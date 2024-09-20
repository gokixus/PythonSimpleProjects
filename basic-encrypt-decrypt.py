def encrypt(text, value, output=""): #sifreleme islemi. value degeri kadar harfleri ileriye donustur.
    for char in text:
        output = f"{output}{chr(ord(char) + value)}"
    return output

def decrypt(text, value, output=""): #sifre cozme islemi
    for char in text:
        output = f"{output}{chr(ord(char) - value)}"
    return output

i = int(input("Increment Value: ")) #kaç harf ileri veya geri gidilsin?

text = input("Type your text: ") #şifrelenecek cümle
print(f"Encrypted text: {encrypt(text, i)}") #şifrelenmiş cümle

text = input("\nType for decrypt: ") #deşifrelenecek cümle
print(f"Decrypted text: {decrypt(text, i)}") #deşifrelenmiş cümle
