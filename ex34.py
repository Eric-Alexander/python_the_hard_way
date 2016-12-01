from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input(">> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print """
    There is a bear here.
    The bear has a bunch of honey.
    The fatass bear is in front of another door.
    How are you going to move the bear?
    """
    bear_moved = False

    while True:
        choice = raw_input(">> ")

        if choice == "take honey":
            dead("The bear glares at you and claws your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved away from the door. Go through it and save yourself!"
            bear_moved = True
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I havent the slightest clue what that means."

def odins_raven_room():
    print """
    Here you find yourself face to face with the great and lamenting Raven of Odin! Don't meet its' eye or you risk going insane. Do you flee or devour your own sanity?
    """
    choice = raw_input(">> ")

    if "flee" in choice:
        start()

    elif "head" or "sanity" in choice:
        dead("What a tasty treat!")
    else:
        odins_raven_room()

def dead(why):
    print why, "Goooood Jobbo!"
    exit(0)

def start():
    print """
    You are in a dark room.
    There is a door to your right.
    There is a door to your left.
    Which one do you take?
    """
    choice = raw_input(">> ")

    if "l" or "L" or "left" in choice:
        bear_room()
    elif "r" or "R" or "right" in choice:
        odins_raven_room()
    else:
        dead("You meekly stumble around the room until you starve to death")

start()
