from room import Room
from flashlight import Flashlight
from character import Enemy
from container import Container
from phone import Phone
from book import Book
<<<<<<< HEAD
from motorcycle import Motorcycle
=======
from razor import Razor
>>>>>>> a9f6e9cceb3a66408297ca4694f6d49a17ca6c76

heldItems = []
myHealth = 53
visitedRooms = []

# ********************************* SET UP THE ROOMS *********************************



# Kitchen
#
# Room descriptions should include interactive containers like CABINET, BIN, DESK, SHELF, SHOEBOX that contain/hide other interactive items
kitchen = Room("Kitchen","A dark and dirty room with flies buzzing around. There are dirty beakers, graduated cylinders, and pipettes in the sink. There is a CUPBOARD above the sink and a CABINET under the sink.")

# The kitchen has a CUPBOARD object that contains/hides 3 interactive items, a sponge, a plate, a can of soup
# Once this container is open, the interactive items will no longer be hidden in the container
kitchen.cupboard = Container("cupboard above the sink",["sponge","plate","can of bOPW soup"])
# The kitchen has a CABINET object that contains/hides 2 interactive items, a knife and a twinkie
# Once this container is open, the interactive items will no longer be hidden in the container
kitchen.cabinet = Container("cabinet under the sink",["knife","twinkie"])
# Create an interactive item that's show in a room (not hidden in a container) with create_room_item()
kitchen.create_room_item("spoon")
kitchen.create_room_item("rat")


# Bathroom
#
# Room descriptions should include interactive containers like CABINET that contain/hide other interactive items
bathroom = Room("Bathroom","A squeaky clean room. There are Sinks , Showers , and Tolites.")

# The bathroom has a CABINET object that contains/hides 1 interactive item, a razor
# Once this container is open, the interactive items will no longer be hidden in the container
bathroom.cabinet = Container("cabinet above the sink",["a razor"])
# Create an interactive item that's show in a room (not hidden in a container) with create_room_item()
bathroom.create_room_item("rat")



# Garage
#
# Room descriptions should include interactive containers like CABINET, BIN, DESK, SHELF, SHOEBOX that contain/hide other interactive items
garage = Room("Garage","A dark room with what looks to be a workbench in the corner with tools and a small lamp on it, and in the center of the room there is a motorcycle. There is also a TOOLBOX on the desk")

# The garage has a TOOLBOX object that contains/hides 1 interactive item, a set of keys for the motorcycle
# Once this container is open, the interactive items will no longer be hidden in the container
garage.desk = Container("toolbox on the desk",["motorcycle keys"])
garage.container = Container("motorcycle", ["MOTORCYCLE"],"in")
# Create an interactive item that's show in a room (not hidden in a container) with create_room_item()
garage.create_room_item("wrench")
garage.create_room_item("broken glass")


# Small Office
#
smalloffice = Room("Small Office","A dark room with a mess of books and papers covering the desk. There is some mail and an ozon.ru PACKAGE. You can READ a book. You can look in the DESK.")
smalloffice.desk = Container("desk",["battery","envelope"])
smalloffice.package = Container("ozon.ru package",["sheet of bubble wrap","porcelain figurine of a bear","red flashlight"])
smalloffice.create_room_item("guinea pig")
redFlashlight = Flashlight("red",0,False)



# Laboratory
#
lab = Room("Laboratory","A bright room with sunlight shining through windows secured by prison bars. There is a messy SHELF on the north wall.")
# The lab has a SHELF object that contains 3 interactive items. Shelf gets a third argument because you'd say ON the shelf, not IN the shelf
lab.shelf = Container("shelf",["brass key","spork","yellow flashlight"],"on")
lab.create_room_item("rat")
yellowFlashlight = Flashlight("yellow",1,True)



# Supply Closet
#
supplycloset = Room("Supply Closet","A small dark room with a musty smell. On one side is a filing CABINET and a large plastic BIN. On the other side is a SHELF with supplies and a SHOEBOX.")


# Boiler Room
#
boilerroom = Room("Boiler Room","A musky dark room covered in cobwebs. A BOILER is set up in the northwest corner of the room with an electrical PANEL next to it.")
#boiler room has an electrical panel that has one item in it.
boilerroom.panel = Container("panel",["phone"],"in")
phone = Phone(True,False)

# Create a fake room called locked that represents all permenently locked doors
#
locked = Room("locked","")



# Library
#
library = Room("Library","A dark and dirty room with CobWebs and spiders all around. There are Chemistry Books, Old Computers, and a DRAWER.")
# Once this container is open, the interactive items will no longer be hidden in the container
library.drawer = Container("Drawer",["baseball bat","Book"])
# Create an interactive item that's show in a room (not hidden in a container) with create_room_item()
book = Book(True,"red")
library.create_room_item("empty purse")




# Waitting Room 
#
# Room descriptions should include interactive containers like CABINET, BIN, DESK, SHELF, SHOEBOX that contain/hide other interactive items
waittingroom  = Room("waitting room","A dark and dirty room with flies buzzing around. There are chairs, old dusty lamps, and tables inthe middle of the room. There is are BOXES laying around and PAPERS piled all over the place.")

# The waitting room has a BOX object that contains/hides 3 interactive items, a key to the geroge,
# Once this container is open, the interactive items will no longer be hidden in the container
waittingroom.box = Container("Box under a chair",["key to garage"])
# The waitting Room has stcks of papers object that contains/hides 2 interactive items
# Once this papers are removed, the interactive items will no longer be hidden in the container
waittingroom.papers = Container("papers piled everywhere",["item 1","item 2"])
waittingroom.container = Container("garage", ["GARAGE"],"in")


# Create an interactive item that's show in a room (not hidden in a container) with create_room_item()
waittingroom.create_room_item("spoon")
waittingroom.create_room_item("rat")






# Connect rooms. These are one-way connections.
kitchen.link_room(locked, "EAST")
kitchen.link_room(smalloffice, "SOUTH")
kitchen.link_room(bathroom, "WEST")
supplycloset.link_room(boilerroom, "NORTH")
supplycloset.link_room(smalloffice, "EAST")
smalloffice.link_room(kitchen, "NORTH")
smalloffice.link_room(lab, "EAST")
smalloffice.link_room(locked, "SOUTH")
smalloffice.link_room(supplycloset, "WEST")
lab.link_room(bathroom, "SOUTH")
lab.link_room(smalloffice, "WEST")
boilerroom.link_room(supplycloset, "SOUTH")
lab.link_room(library, "NORTH")
library.link_room(lab, "SOUTH")
bathroom.link_room(lab,"NORTH")
bathroom.link_room(locked,"WEST")
bathroom.link_room(kitchen,"EAST")
current_room = kitchen








# Set up characters
dmitry = Enemy("Dmitry", "A smelly zombie")
dmitry.set_speech("Brrlgrh... rgrhl... brains...")
dmitry.set_weaknesses(["FORK","SPORK","KNIFE", "SPOON","baseball bat"])
supplycloset.set_character(dmitry)

zombiecat = Enemy("Zombie Cat","A cute cat that's rotting.")
zombiecat.set_speech("Meoagh...!")
zombiecat.set_weaknesses(["FORK","SPORK","KNIFE","SPOON"])
boilerroom.set_character(zombiecat)

# This is a procedure that simply prints the items the player is holding and tells them if they can do something with that item
def playerItems():
    # Print out the player's Held Items and let player know if they can USE an item to fight a character or something
    if len(heldItems) == 1:
        print("You are holding a "+heldItems[0])
        print("You can DROP "+heldItems[0].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name)
    elif len(heldItems) >= 2:
        print("Your hands are full. You must drop something before you can pick anything else up.")
        print("You are holding a "+heldItems[0]+" and a "+heldItems[1])
        print("You can DROP "+heldItems[0].upper()+" or DROP "+heldItems[1].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name+" or USE "+heldItems[1].upper())
    # ********************************* SPECIAL ITEM INTERFACES *********************************
    # If holding a special item, then display the item's interface with get_interface()
    if "red flashlight" in heldItems:
        redFlashlight.get_interface(heldItems,current_room)
    if "yellow flashlight" in heldItems:
        yellowFlashlight.get_interface(heldItems,current_room)
    ##if "book" in heldItems:
       ## book.get_interface()

# This fuction checks the player's command and then runs the corresponding method
def checkUserInput(current_room,command,heldItems):
    # Convert it to ALL CAPS
    command = command.upper()
    # All possible user input commands go here
    print("\n")
    
    # ********************************* SPECIAL USER INPUT *********************************
    # If holding a special item, then check for that item's UI keywords with check_input()
    if "red flashlight" in heldItems and "RED FLASHLIGHT" in command:
        redFlashlight.check_input(command,heldItems,current_room)
    elif "yellow flashlight" in heldItems and "YELLOW FLASHLIGHT" in command:
        yellowFlashlight.check_input(command,heldItems,current_room)
    elif "book" in heldItem and "OPEN" in command:
        book.check_input(command,heldItems)
        

    # ********************************* USE, TAKE, DROP *********************************
    # Use an item to fight an enemy
    elif "USE " in command and current_room.get_character() is not None:
        # command[4:] is used to get the characters typed after "USE "
        enemyHealth = current_room.character.fight(command[4:])
        if enemyHealth < 1:
            print(current_room.character.name+" is dead")
            current_room.remove_character() # If the enemy is dead, then remove them from the room
    # Take lets you pick up an item
    elif "TAKE " in command:
        # command[5:] is used to get the characters typed after "TAKE "
        heldItems = current_room.take_room_item(command[5:],heldItems)
    # Drop lets you set down an item
    elif "DROP " in command:
        # command[5:] is used to get the characters typed after "DROP "
        heldItems = current_room.add_room_item(command[5:],heldItems)
    # Talk and Fight aren't currently used in this version of the game, but could be implemented in your version of the game
    elif "TALK" in command and current_room.get_character() is not None:
        current_room.character.talk()
    elif "FIGHT" in command and current_room.get_character() is not None:
        current_room.character.talk()
    
    # ********************************* ROOM SPECIFIC USER INPUTS *********************************
    # Interactive containers look like this...   elif current_room.name == "Laboratory" and command == "SHELF"
    elif current_room.name == "Kitchen" and command == "CUPBOARD":
        # Open kitchen.cupboard and concat each of the contents to the end of room_items
        current_room.room_items += kitchen.cupboard.open()
    # Can only open cabinet if holding a flashlight that isOn
    elif current_room.name == "Kitchen" and command == "CABINET" and (("red flashlight" in heldItems and redFlashlight.isOn) or ("yellow flashlight" in heldItems and yellowFlashlight.isOn)):
        # Open kitchen.cabinet and concat each of the contents to the end of room_items
        print("You use the flashlight to look inside the cabinet.")
        current_room.room_items += kitchen.cabinet.open()
    elif current_room.name == "Kitchen" and command == "CABINET":
        print("You check the cabinet, but it's too dark to see if there is anything inside.")
    elif current_room.name == "Small Office" and command == "PACKAGE":
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        current_room.room_items += smalloffice.package.open()
    elif current_room.name == "Small Office" and command == "READ":
        print("POCCNR??? You can't read it. It's written is some strange Cyrillic script.")
    elif current_room.name == "Small Office" and command == "DESK" and "brass key" in heldItems:
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        print("You use the brass key to unlock the desk.")
        current_room.room_items += smalloffice.desk.open()
    elif current_room.name == "Small Office" and command == "DESK":
        print("The desk drawer is locked.")


         elif current_room.name == "waittingroom" and command == "GARAGE" and "garage keys" in heldItems:
       # use keys to go to garage
        print("You go into the garage")
        current_room = garage
    elif current_room.name == "waittingroom" and command == "GARAGE:
        print("The door to the garage needs a key")

    elif current_room.name == "garage" and command == "MOTORCYCLE" and "motorcycle keys" in heldItems:
       # use motorcycle to go to town
        print("You use the motorcycle key and go to town.")
        current_room = town
    elif current_room.name == "garage" and command == "MOTORCYCLE":
        print("The motorcycle needs a key")
        
    elif current_room.name == "Laboratory" and command == "SHELF":
        # Open lab.shelf and concat each of the contents to the end of room_items
        current_room.room_items += lab.shelf.open()

    elif current_room.name == "Boiler Room" and command == "PANEL":
         current_room.room_items += boilerroom.panel.open()

    elif current_room.name == "Library" and command == "DRAWER":
        current_room.room_items += library.drawer.open()

    # ********************************* MOVE *********************************
    else:
        current_room = current_room.move(command,visitedRooms) # If it was none of those commands, assume it was a direction. Try to move.
    return current_room


#THE LOOP
while True:
    print("\n")
    # Print current room info
    myHealth = current_room.info(heldItems,myHealth,visitedRooms) # this returns myHealth cuz an enemy in the room could hurt you
    if myHealth <= 0:
        print("You died.\nGAME OVER")
        break
    # Print player items
    playerItems()
    # Get user input
    command = input("> ")
    # Check the user input
    current_room = checkUserInput(current_room,command,heldItems)


