print("1-Square\n2-Rectangle\n3-Circle")

while True:
    choice = input("Your choice: ")
    if choice == "1":
        aside = int(input("A side: "))
        print(f"Area of square is {aside**2}\n")
    elif choice == "2":
        aside = int(input("A side: "))
        bside = int(input("B side: "))
        print(f"Area of rectangle is {aside*bside}\n")
    elif choice == "3":
        r = int(input("Radius: "))
        pi = 3.14
        print(f"Area of circle is {(r**2)*pi}\n")
    else:
        print("Exit has been made.")
        break
