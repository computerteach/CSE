from datetime import datetime

#defining the class properites inside
class Post:
    
    #initalizing the variable
    post_id = 0
    
    #__init__ is normally the first method in class
    # it is initalizing these data attributes
    #self is referring to the object
    def __init__(self, user_name, message):
        self.message = message
        self.user_name = user_name
        self.timestamp = datetime.now()
        self.post_id = Post.post_id
        Post.post_id += 1
    
    #What is this method returning?
    def __str__(self):
        return self.user_name + " " + self.timestamp.__str__() + ": " + self.message
    
    #What does this method do?
    def set_message(self, message):
        self.message = message
    
    #What infomration will this method return?
    def get_user_name(self):
        self.user_name = user_name
    
    #What will this method return?
    def get_post_id(self):
        return self.post_id
