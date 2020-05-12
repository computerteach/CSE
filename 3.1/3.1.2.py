# song = 2 + 1 
#song = 3.0 
song = "geese" 
print(song)
#variable types
mystery_value = type("Hello World!")
print(mystery_value)

print(type("1"))
print(type(-10))
print(type(False))
print(type("False!"))
print(type(3.14))
#Input function
x = input("What is your name? ") 
y = input("What is your age? ")

print("Hello ", x)
print("You are", y, "years old")
#Converting Data Types
first_age = input("What is the age of person 1? ")
second_age = input("What is the age of person 2?  ")

difference = int(first_age) - int(second_age)

print("Person 1 is", difference, "years older than person 2.")

student_count = str("8675307") 
print(student_count) 

introduction_question = input("What is your name?") 
print(introduction_question) 
pi = int(3.14159)
print(pi)
print(bool(0 == 4-3))
print(bool(3/3 == 1))
print(float(10))
#18 
studs_in_class1 = 27
studs_in_class2 = 31
studs_in_class3 = 13
sum_of_students = studs_in_class1 + studs_in_class2 + studs_in_class3

average_student_count = int(sum_of_students / 3)
print(average_student_count)

#19 - Nesting
print(type(input("type in a name: "))) 
print(type(input("type in a number: "))) 
print(type(input("Enter anything: ")))

#20 Boolean conditionals and logical operators
x = int(input("pick a number:"))

if (x < 10): 
  print("too low")
else: 
  print("too high")
  
  #Corrected 21
  guess = int(input("Pick a number: "))

if (guess < 10): 
  print("too low") 
elif (guess == 10): 
  print("Exactly 10!") 
else: 
  print("too high")
  
  #22 Boolean
  print(False) 
print(4==4) 
print(2+6==8) 
print(5!=3) 
print(5>4) 
print(4<=5)
