def largest(n):
    index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[index]:
            index = i
    return index
        


numbers = (input("Numbers: ")).split()
largest_index = largest(numbers)
print(f"Largest number is {numbers[largest_index]} at index {largest_index}")
