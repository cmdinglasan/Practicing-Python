#Ask the user for the input (dividend)
#Dividend must be a number
#Divisor is the number to divide the dividend by
#Divisor must be a number

def compute(number):
    valid_divisors = []

    for x in range(1, number + 1):
        
        if number % x == 0:
            valid_divisors.append(x)

    return valid_divisors

number = int(input("Enter a dividend: "))

print(f"The valid divisors of {number} is/are {compute(number)}")