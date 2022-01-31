# Ask user for a number.
# Print out if number is odd or even

def check_num_if_odd_or_even(num):
  num_type = None

  remainder = num % 2

  if(remainder == 0):
    num_type = "even"
  else:
    num_type = "odd"

  return str(num) + " is an " + str(num_type) + " number"

def get_number():
  number = int(input("Give me a number: "))

  return check_num_if_odd_or_even(number)

# Ask number from user
print(get_number())