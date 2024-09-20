import random

def generate_name():
    firstNames = ["Ali", "Furkan", "Ahmet", "Hilal", "Furkan", "Burak", "Esin", "Cemre", "Sevda", "Derya"] #rastgele isim ve soyisimler
    lastNames = ["Yılmaz", "Kaya", "Kaplan", "Boz", "Altın", "Akdemir", "Yıldırım"]
    randomFirstNames = random.choice(firstNames)
    randomLastNames = random.choice(lastNames)
    return f"{randomFirstNames} {randomLastNames}"

for i in range(5):
    print(generate_name())