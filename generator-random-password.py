import random, string

def generate_password(length, level, output = []):
    chars = string.ascii_letters
    if level > 1:
        chars = f"{chars}{string.digits}"  #level 2 ve üstü rakamlar eklenir
    if level > 2:
        chars = f"{chars}{string.punctuation}" #level 3 ve üstü de özel karakterlerde eklenir. 
    for i in range(length):
        output.append(random.choice(chars)) #length kaç ise o kadar rastgele harfler eklenir.
    return "".join(output)
    

password_length = int(input("Length: "))
password_level = int(input("Level: "))
password = generate_password(password_length, password_level)
print(f"\nYour password: {password}")