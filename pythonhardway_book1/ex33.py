i = 0
numbers = []

while i < 7:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom 1 is {i}")
    
print("The numbers : ")

for num in numbers:
    print(num)
    