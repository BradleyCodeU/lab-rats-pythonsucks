class  Razor():
    #constructor
    def __init__(self,deadRazor):
        self.deadRazor = deadRazor #true or false
        self.isOn = False

    #getter that tells you if the phone has batteries or not
    def get_batteries(self):
        if not self.deadRazor:
            print("The Razor does have a battery in it. It should turn on.")
        else:
            print("The Razor doesn't have any batteries in it.")
            
        
    #setter that turns on the phone
    def turn_on(self):
        if not self.isOn:
            if not self.deadRazor:
                self.isOn = True
                print("You turn on the Razor on and wait until it finishes its start up.")
            else:
                print("You attempt to turn on the Razor but it doesn't work. You should check the batteries.")

    #setter that turns off the phone
    def turn_off(self):
        if self.isOn:
            self.isOn = False
            print("You switch the Razor off. It stops buzzing.")
