# Ask the user's  name and age
# Then get the year when the user will be 100 years old

from datetime import date

def get_name():
  name = input("What\'s your name? ")

  return name

def get_age():
  # Validate if age is less than or equal to 100
  while True:
    age = int(input("How old are you today? "))
    try:
      if age < 101 | age >= 0:
        break
      else:
        print("Age can\'t be less than 0 or greater than 100. Try again.\n")
    except:
      print("Age must be a number. Try again.")
  return age

def calculate(name, age):
  while True:
    try:
      # Subtract 100 to user's age
      years = 100 - age;

      # Get current date
      current_date = date.today()

      # Add the years remaining to current year
      years_to_100 = current_date.year + years

      if(years_to_100 != current_date.year):
        return name + ", you will be 100 years old in the year " + str(years_to_100)
      else:
        return name + ", you are currently 100 years old."
    except ValueError:
      print("Error calculating")

# Get user's name
name = get_name()

# Get user's age
age = get_age()

print(calculate(name, age))