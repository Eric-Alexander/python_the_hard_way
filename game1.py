from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Sublass it and implement enter()."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished.')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):

    snarky_quips = [
        "Whelp...you died. Not the best option for saving the starship, are you?",
        "LOLZ you just got PWNED, NERD.",
        "Don't hate your avatar. Hate youself. Game Over",
        "That was the most pitiful attempt I've witnessed. LOSE."
    ]

    def enter(self):
        print Death.snarky_quips[randint(0, len(self.snarky_quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print """
            The Ooblekians of Star Sec #666 have invaded your starship and obliterated your entire crew. As the last surviving member of your ship, you're only chance of survival is to retreive and arm the Neutron Total Oblirator Bomb from the Weapons Army, place it on The Bridge and destroy the startship after getting into an escape pod and jutting off to safety. \n\n
            As you run down the Central Corridor to the Weapons Armory a nast Ooblekian surprises you, obstructing your path! He notices you and attempts to pull out his Zoorbleg gun to decimate you. What will you do??
        """

        action = raw_input(" >> ")

        if action == "shoot":
            print """
                You unsling your Rayeon blaster from your
                hip intuitively and aim for his chest. But as you pull the trigger the Ooblekian warps space-time itself as to dodge the plasma blast for your Rayeon blaster and rebuttals with a slough of Zoorbleg pellets that riddle your body and drop you to the floor!

            """
            return 'death'
        elif action == "run":
            print """
                Channeling Neo from 'The Matrix' movie put on for Video Night in the rec room last week you, seemingly, manipulate space-time and bend around every single Zoorblerg pellet the Ooblekian shoots at you! When his clip empties you return to a natural position to balance yourself. But, as you do this your foot catches on one of the Zoorblerg cartridges and you slip and fall! The time is opportune for the Ooblekian as he slithers up to you, wraps his tenacle around your nack and slowly squeezes your conscienceness into oblivion.
            """
            return 'death'

        elif action == "insult":
            print """
            Having studied at the prestigious Counter Measure Academy for Hostile Creatures you know that an Ooblekians biggest weakness is insulting its' hive mother in its' native tongue. You begin to shout the insult as such: 'OPWEJF FII FSD GJWOIGJ IRJG ERIGJ GJIERJS FJIJFS De!!!!!!!' The visualization of such an insult to its' hive mother is too unbearable to realize and self-administers a salt capsule thereby bubbling and melting its' wiggly course into a pile of oozey muck. Yay! You now progress past the gelatinous and enter the Weapons Armory

            """
            return 'laser_weapon_armory'
        else:
            print "INVALID ACTION. TRY YOUR LUCK AGAIN"
            return 'central_corridor'



class LaserWeaponArmory(Scene):
    def enter(self):
        print "LASER ASRENAL"

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass
class Finished(Scene):
    def enter(self):
        print "WINNER"
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'death': Death(),
        'finished': Finished()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
