# Create class / give it a name / And indicate objects
class Song(object):

#define functions of the class. Requires the self call - sets the instance variable
    def __init__(self, lyrics):
        self.lyrics = lyrics
 #define         
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_bday = Song(["Happy Birthday to you",
                    "I don't want to get sued",
                    "So I will stop there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

