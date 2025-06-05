def two_min_numbs(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(0, length - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers[0] + numbers[1]
input_str = input("Введіть щонайменше 4 додатних числа через пробіл: ")
numbers = [int(x) for x in input_str.split()]

if len(numbers) < 4:
    print("Потрібно ввести щонайменше 4 числа!")
else:
    result = two_min_numbs(numbers)
    print("Сума двох найменших чисел:", result)