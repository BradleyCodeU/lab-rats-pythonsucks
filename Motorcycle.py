class Motorcycle():
    #constructor
    def __init__(self,color,fuel):
        self.color = color # string
        self.fuel = fuel # int
        self.chain = True

    #getter that tells you if the motorcycle has fuel
    def get_fuel(self):
        return self.fuel

    #getter that tells you what color the motorcycle is
    def get_color(self):
        return self.color

    # setter that sets motorcycle color
    def change_Color(self, newColor):
        self.color = newColor

    
    #unchain the motorcycle
    def set_chain(self):
        self.chain = not.self.chain
        

    
