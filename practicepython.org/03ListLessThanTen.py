# Main List
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# New list for computation
b = []

userNum = int(input("Give me a number: "))

for num in a:
  if num < userNum:
    b.append(num)

print("The numbers less than " + userNum + "are " + b)