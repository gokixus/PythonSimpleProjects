print("1- Celsius to fahrenheit") #menu selection
print("2- Fahrenheit to celsius")
choice = input("Your shoice (1/2): ")

if choice == "1":
    celsius = float(input("Degree to convert: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius} degree celcius is equal to {fahrenheit}")
elif choice == "2":
    fahrenheit = float(input("Degree to convert: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} degree celcius is equal to {celsius}")
else:
    print("Please choose between 1 and 2.")