num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print(f"Add: {num1} + {num2} = {num1 + num2}")
print(f"Subtract: {num1} - {num2} = {num1 - num2}")
print(f"Multiply: {num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"Divide: {num1} / {num2} = {num1 / num2}")
    print(f"Remainder: {num1} % {num2} = {num1 % num2}")
else:
    print(
        "Division and remainder operations are not possible "
        "(division by zero)."
    )

print(f"Power: {num1} ** {num2} = {num1 ** num2}")
