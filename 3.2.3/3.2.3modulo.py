#################################################################################
#    a3.2.3_TR_practice_with_while.py
#    Example solution
################################################################################

# numbers 1 to 5 inclusive
print("Numbers 1 to 5 inclusive")
number = 1
while (number <= 5):
  print(number)
  number = number + 1

# numbers 10 to 1 inclusive
print("\nNumbers 10 to 1 inclusive")
number = 10
while (number >= 1):
  print(number)
  number = number - 1
  
# even numbers from 2 to 10 inclusive
print("\nEven numbers from 2 to 10 inclusive")
while (number <= 10):
  if (number % 2 == 0):
    print(number)
    number = number + 1

# odd numbers from 9 to 1 inclusive
print("\nOdd numbers from 9 to 1 inclusive")
while (number >= 1):
  if (number % 2 == 1):
    print(number)
    number = number - 1