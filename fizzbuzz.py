def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

length = int(input("Length of array: ")) #dizi uzunlugu

for i in range(1, length+1):
    print(fizzbuzz(i))