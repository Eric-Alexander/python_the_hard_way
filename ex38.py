ten_words = "Ooblek CherryTart Osmosis Applebottom Enqueue Alibaster"

print "Hold on... there are not then words in this list...let's fix that!"

splitz = ten_words.split(' ')
more_words = ["Cauliflower", "Pippenwort", "Chinadoll", "Matterhorn", "Johnnybegood"]

while len(splitz) != 10:
    next_one = more_words.pop()
    print "Adding: ", next_one
    splitz.append(next_one)
    print "There are %i items now." % len(splitz)

print "There we go: ", splitz

print "Let's manipulate more things with variable splitz"

print splitz[1]
print splitz[-1]
print splitz.pop()
print ' '.join(splitz)
print '#'.join(splitz[4:7])
print pop(splitz)
