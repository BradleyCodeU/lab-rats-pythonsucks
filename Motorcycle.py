class Phone():
    #constructor
    def __init__(self,color,fuel):
        self.color = color # string
        self.fuel = fuel # int

    #getter that tells you if the motorcycle has keys
    def get_keys(self):
        if not keys:
            print("You have no keys")
        else:
            print("You have the keys")

    #getter that tells you if the phone has a signal
    def get_signal(self):
        if self.deadPhone or self.isOn == False:
            print("You can't check the signal when the phone is off.")
        elif self.isOn and self.signal == False:
            print("You don't any signal here.")
        else:
            print("Yay, you're getting signal here.")
            
        

    #setter that turns on the phone
    def turn_on(self):
        if not self.isOn:
            if not self.deadPhone:
                self.isOn = True
                print("You turn on the phone on and wait until it finishes its start up.")
            else:
                print("You attempt to turn on the phone but it doesn't work. You should check the batteries.")

    #setter that turns off the phone
    def turn_off(self):
        if self.isOn:
            self.isOn = False
            print("You switch the phone off. Its light stops shining.")
