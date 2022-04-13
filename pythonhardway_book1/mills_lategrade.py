totalearned = int(input("What was your grade? (out of 100): "))
late = input("Was your assignment turned late? (true or false):  ")
if late == 'false':
    print("Your assignment was turned in on time, your grade is {totalearned}/100".format(totalearned=totalearned))
else:
    totalearned = totalearned/2
    print("Your assignment was not turned in on time, your grade is {totalearned}/100".format(totalearned=totalearned))
