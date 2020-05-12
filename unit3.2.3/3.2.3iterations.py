#################################################################################
#    a3.2.3_TR_combo_menu_while_loop.py
#    Example solution
################################################################################

order = []
loop_check = True

while (loop_check):
  # iteration 1 
  sandwhich = input("Please pick a type of sandwhich, chicken for $5.25, beef for 6.25, or tofu for 5.75.")
  if (sandwhich in ["chicken", "beef", "tofu"]):
    sandwhich_bought = True
    order.append(sandwhich)
    print(sandwhich)
  else:
    sandwhich_bought = False
    print("That's not a sandwhich we sale here.")
  
  # iteration 2
  beverage = input("Would you like a drink, yes or no?")
  if (beverage == "yes"):
    beverage_bought = True
    beverage = input("would you like a small for $1.00, a medium for $1.75, or a large for $2.25?")
    if (beverage in ["small", "medium", "large"]):
      print("You said", beverage, "drink.")
      order.append(beverage)
    else:
      beverage_bought = False
      print("That's no a drink size option.")
  else:
    beverage_bought = False
    print("You did not want a drink.")
    
  # iteration 2 cost
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
    
  # iteration 3
  fries = input("Would you like french fries, yes or no? ")
  if (fries == "yes"):
    fries_bought = True
    fries = input("Would you like a small for $1.00, a medium for $1.50, or a large for $2.00? ")
    print("You said", fries, "fries.")
  else: 
    fries_bought = False
    print("you did not want fries.")
  
  if (fries == "small"):
    total = total + 1
  elif (fries == "medium"):
    total = total + 1.50
  elif (fries == "large"):
    total = total + 2
  
  # iteration 4
  ketchup_string = input("How many ketchup packets would you like? ")
  try:
    ketchup = int(ketchup_string)
  except ValueError:
    order.append(ketchup_string)
    ketchup_cost = ketchup * .25
    total = total + ketchup_cost
  
  if (sandwhich_bought == True):
    if (beverage_bought == True):
      if (fries_bought == True):
        print("You bought:", sandwhich, "sandwhich,", beverage, "beverage,", fries, "fries, and", ketchup, "ketchup packets.")
        total = total - 1
      else:
        print("You bought:", sandwhich, "sandwhich", beverage, "beverage, no fries, and", ketchup, "ketchup packets.")
    elif (fries_bought == True):
      print("You bought:", sandwhich, "sandwhich, nothing to drink,", fries, "fries, and", ketchup, "ketchup packets.")
    else:
      print("You bought:", sandwhich, "sanwhich, nothing to drink, no fires, and", ketchup, "ketchup packets.")

  print(order)
  print(total)
  
  # the condition at the end that will trigger the loop to repeat or stop
  again = input("Is another person ready to order? yes or no")
  if (again == "yes"):
    loop_check = True
  else:
    loop_check = False
    print("Closing Time!")
  