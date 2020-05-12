from Post import Post

all_posts_archive = []

# your code here
username = input("What is your username?")
print("What would you like to do? ")
print("add - Add a post to the archive")
print("remove - Remove a post from the Archive.")
print("change user - Change the user name associated with any future posts")
print("Display the current up to date list of all posts")
print("quit - End the Program!")
user_input = input("your Responses: ")

while (user_input != "quit"):
  #if/elif/else to check decisions of user
  if (user_input == "add"):
    message = input("What's your message")
    post = Post(username, message)
    all_posts_archive.append(post)
    
  elif (user_input == "remove"):
      index = input("What was the index of the message to remove?")
      del all_posts_archive[int(index)]
      
  elif (user_input =="change user"):
      username = input("What's your new username?")
    
  elif (user_input == "print"):
      for post in all_posts_archive:
        print(post)
      
  else:
      print("Your decision was ne a valid one.")
      
  #PROMPT THE USER FOR A DECISION AGAIN
  print("\n\What would you like to do?")
  print("add - Add a post to the archive")
  print("remove - Remove a post from the archive")
  print("change user - Change the user name associated with any future posts")
  print("print - Display the current up to date list of all posts")
  print("quit - End the program")
  user_input = input("Your responses: ")