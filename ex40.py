class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_song(self):
        for line in self.lyrics:
            print line
promises = Song(["Sleeping thru the evening",
                "Seeing dreams inside my head",
                "I'm heading out, I've got some Ins",
                "Who say they care and they just might."])

party = Song(["Do you want to come to a party?",
            "My friends pick me up in the truck at 11:30",
            "It's at a frathouse, the people are cool there",
            "I walked up and lined in I would never dream there."])

promises.sing_song()
party.sing_song()
