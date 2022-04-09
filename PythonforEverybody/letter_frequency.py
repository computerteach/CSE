words = input("what is your phrase?")
count = 0
for letter in words:
    if letter == 'a':
        count = count + 1
print(count)