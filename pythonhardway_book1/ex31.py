print(""" You enter a dark room with two doors.)
Do you go through door #1 or Door  #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do? Pick 1 or 2")
    print("1. Take the cake.")
    print("2. Scream at the bear")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job")
    else:
        print(f"Well, doing {bear} is probably better. ")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of Jello.")
        print("Good Job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good Job!")
        
else:
    print("You stumble around and fall on a knife and die. Good Job!")
    
        