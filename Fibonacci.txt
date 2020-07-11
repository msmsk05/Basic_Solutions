fibonacci = []
number1 = 0
number2 = 1
while True:
    fibonacci.append(number2)
    num = number1 + number2
    number1 = number2
    number2 = num
    if num > 55:
        break
print(fibonacci)