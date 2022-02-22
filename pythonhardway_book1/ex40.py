#Modules
mystuff = {'apple': "I am Aples!"}
print(mystuff['apple'])

import mystuff
mystuff.apple()

def apple():
    print("I am Apples")

#This is just a variable
tangerine = "Living refelction of a dream!"

import mystuff
mystuff.apple()
print(mystuff.tangerine)

mystuff['apple'] #get apple from the dictionary
mystuff.apple() # get apple from the module
mystuff.tangerine #same thing, it's just a variable

class MyStuff(object):

    def _init_(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I am apples!")
