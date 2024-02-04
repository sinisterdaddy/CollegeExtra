# income = int(input("Enter user's salary: "))

# if income <= 500000:
#     tax = 0
# elif income <= 750000:
#     tax = (income - 500000) * 0.10
# elif income <= 1000000:
#     tax = 250000 * 0.10 + (income - 750000) * 0.20
# else:
#     tax = 250000 * 0.10 + 250000 * 0.20 + (income - 1000000) * 0.30

# print(f"Tax: {tax}")

num = int(input("Enter an integer: "))
digits = [int(digit) for digit in str(num)[::-1]]
print(" ".join(map(str, digits)))

