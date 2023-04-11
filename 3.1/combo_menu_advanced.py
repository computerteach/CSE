total = 0.0
selected_a_sandwich = True
selected_a_beverage = True
selected_french_fries = True

sandwich = input("Would you like a chicken, beef, or tofu sandwich? ")
if sandwich == "chicken":
    total += 5.25
elif sandwich == "beef":
    total += 6.25
elif sandwich == "tofu":
    total += 5.75
else:
    selected_a_sandwich = False
    print ("You did not select a sandwich type")
    
    
french_fries = input("Would you like fries? (yes or no): ")
if french_fries == "yes":
    french_fry_size = input("What size french-fries would you like? ")
    if french_fry_size != "small" and french_fry_size != "medium" and french_fry_size != "large":
        print ("Error Code 5904: illegal value for french_fry_size")
        selected_french_fries = False
        #quit()
    elif french_fry_size == "small":
        mega_size = input("Would you like to MEGA-Size your fries? (yes or no): ")
        if mega_size == "yes":
            french_fry_size = "large"
            total += 1.00
        total += 1.00
    elif french_fry_size == "medium":
        total += 1.75
    elif french_fry_size == "large":
        total += 2.00
else:
    selected_french_fries = False
    
beverage = input("Would you like a beverage? (yes or no): ")
if beverage == "yes":
    beverage_size = input("What size beverage would you like? ")
    if beverage_size != "small" and beverage_size != "medium" and beverage_size != "large":
        print ("Invalid beverage size, no beverage will be added to your order.")
        selected_a_beverage = False
    elif beverage_size == "small":
        total += 1.00
    elif beverage_size == "medium":
        total += 1.75
    elif beverage_size == "large":
        total += 2.25
else:
    selected_a_beverage = False

if selected_a_beverage and selected_french_fries and selected_a_sandwich:
    total -= 1.00

num_catsup_packets = int(input("How many catsup packets would you like? "))
total += 0.25 * num_catsup_packets

print ("Here is your order:")
if selected_a_sandwich:
    print ("A", sandwich, "sandwich")
if selected_a_beverage:
    print ("A", beverage_size, "beverage")
if selected_french_fries:
    print ("A", french_fry_size, "fry")
print ("And", num_catsup_packets, "catsup packets.")

print ("Your total comes to: $" + str(total))
    
