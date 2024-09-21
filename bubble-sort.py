def bubbleSort(numbers):
    for i in range(1, len(numbers)):
        for j in range(1, len(numbers)- i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers


numbers = [1, 12, 2, 5, 6, 1, 8, 55, 8, 8, 2, 17, 54]
print(f"Sorted array: {bubbleSort(numbers)}")