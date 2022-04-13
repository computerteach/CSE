stuff = list()
while True :
    inp = input('Enter your number:  ')
    if inp == 'done' : break
    value = float(inp)
    stuff.append(value)

average = sum(stuff) / len(stuff)
print('Average:', stuff)