#Create a program to ask the students about their lunch habits
from tkinter.messagebox import YES


eat_lunch_out = input("Do you eat lunch out during school? yes or no  ")
if (eat_lunch_out  =="yes"):
    eat_lunch_out_choice = True
    eat_lunch_out = input("Do you eat at Wendys, McDonalds, Burger King, Subway, Little Caesars, King Soopers, none   " )
    print ("You said: " + eat_lunch_out)
else: 
    eat_lunch_out_choice = False
    print("You must eat at School")



