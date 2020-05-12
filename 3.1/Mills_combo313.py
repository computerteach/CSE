#Iteration 1

sandwhich = input("Please pick a type of sandwhich, chicken for $5.25, beef for $6.25, tofu for $5.75, or no? ")
sandwhich_bought = True
print (sandwhich)


#iteration 2

beverage = input("Would you like a drink, yes or no? ")
if (beverage == "yes"):
    beverage_bought = True
    beverage = input("Would you lika a small for $1.00, a medium for $1.75, or a large for $2.25? ")
    print ("You said " + beverage + " drink. ")
else:
    beverage_bought = False
    print("You did not want a drink. ")

#iteration 2 - cost
total = 0
if (sandwhich == "chicken"):
    total = total + 5.25
elif (sandwhich == "beef"):
    total = total + 6.25
elif (sandwhich == "tofu"):
    total = total + 5.75

if (beverage == "small"):
    total = total + 1
elif (beverage == "medium"):
    total = total + 1.75
elif (beverage == "large"):
    total = total + 2.25


#iteration 3
fries = input("Would you like french fries, yes or no? ")
if (fries == "yes"):
    fries_bought = True
    fries = input("Would you lika a small for $1.00, a medium for $1.50, or a large for $2.00? ")
    print ("You said " + fries + " fries. ")
else:
    fries_bought = False
    print("You did not want fries. ")
    
if (fries == "small"):
    total = total + 1
elif (fries == "medium"):
    total = total + 1.50
elif (fries == "large"):
    total = total + 2


#iteration 4
ketchup_string = input("How many ketchup packets would you like?")
ketchup = int(ketchup_string)
ketchup_cost = ketchup * .25
total = total + ketchup_cost


if (sandwhich_bought == True):
    if (beverage_bought == True ):
        if (fries_bought == True):
            print ("You bought: " + sandwhich + " sandwhich, " + beverage + " drink, " + fries + " fries, and " + ketchup_string + " ketchup packets.")
            total = total - 1
        else:
            print ("You bought: " + sandwhich + " sandwhich, " + beverage + " drink, no fries, and " + ketchup_string + " ketchup packets.")
    elif (fries_bought == True):
        print ("You bought: " + sandwhich + " sandwhich, nothing to drink, " + fries + " fries, and " + ketchup_string + " ketchup packets.")
    else:
        print ("You bought: " + sandwhich + " sandwhich, nothing to drink, no fries, and " + ketchup_string + " ketchup packets.")

print (total)

