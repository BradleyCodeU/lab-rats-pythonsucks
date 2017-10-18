class BOX():
    #constructor
    def __init__(self,Key,BOX):
        self.BOX = found key # true or false
        self.BOX = did not find key #true or false
        self.isOn = False

    #getter that tells you if the BOX has a key or not
    def get_BOX(self):
        if not self.no key:
            print("The BOX does have a key in it. It should have one onside.")
        else:
            print("The BOX doesn't have a key in it.")

    #getter that tells you if the BOX has a key 
    def get_BOX(self):
        if self.BOX or self.isOn == False:
            print("You can't check if theres a key if BOX is closed.")
        elif self.isOn and self.signal == False:
            print("You cant open here.")
        else:
            print("Yay, you can open it here.")
            
        

    #setter that opens the BOX
    def finds_key(self):
        if not self.isOn:
            if not self.find key:
                self.isOn = True
                print("You pick up a Box and see if theres a key inside.")
            else:
                print("You attempt to find the key as unsecsesful. try opening another BOX.")

    #setter opens the BOX 
    def finds_key(self):
        if self.isOn:
            self.isOn = False
            print("You close box. and take key.")
