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

    #setter 
    def turn_opened(self):
        if not self.opened:
            if not self.opened:
                print("You opened your book and the book has no usefull information")
            else:
                print("The book is still closed.")

  
