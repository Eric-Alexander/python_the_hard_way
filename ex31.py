print "You enter a dark room with two doors. Shall you choose the first door or the second door?"

door = raw_input(">> ")

if door == '1':

    print "There is a montsrous werewolf devouring sopapilla!"
    print "1: Take his sopapilla."
    print "2: Politely ask him why he craves sweets."

    werewolf = raw_input(">> ")

    if werewolf == "1":
        print "The werewolf ravenously chews your face off. Holy cow!"
    elif werewolf == "2":
        print "The werewolf rips off your legs with his horrific maw. Yowza!"
    else:
        print "Well, doing %s is likely to be the best outcome." % werewolf
elif door == "2":
    print "Odin's giant one-eyed raven stares deep into your withering soul!"
    print "1: Boysenberries"
    print "2: Onion rinds"
    print "3: Jimmy crack corn"

    insanity = raw_input(">> ")

    if insanity == "1" or insanity == "2":
        print "Your body lives on...but your mind has been melted into primordial soup. OOBLEK~!"
    else:
        print "The insanity of the madness is too intense for you to stomach...you explode into rainbow confetti! AAAaayyyeeee!!!!!"
else:
    print "An undisclosed object wacks you on the back of the head. You blackout only to wake up in bed....realizing it was a dream all along. Phew~!!!"
