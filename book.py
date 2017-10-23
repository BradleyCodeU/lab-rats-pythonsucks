class Book():
    #constructor
    def __init__(self,opened,color):
        self.opened = opened # open and closed
        self.color = color # string

    #getter 
    def get_color(self):
        if self.color == "red" or "RED":
            print("The book is red.")
        elif self.color == "blue" or "BLUE":
            print("The book is blue.")

    def check_input(self,command,heldItems):
        if command == ("OPEN"):
            self.opened = True
        else:
            print("Book is closed")

    def get_opened(self):
        if self.opened == True:
            print("The book has to many words in it and you decide to not read it")
           
  
     
            
