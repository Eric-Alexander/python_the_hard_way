
def print_while(*args):

    i, arr, end, incr = args
    
    while i < end:
        print "At the top of i is %d" % i
        arr.append(i)

        i += incr

        print "Numbers now: ", arr
        print "At the bottom i is %d" % i

    print "The arr: "

    for  num in arr:
        print num
print print_while(0, [], 8, 2)


def print_for(i, arr, end):

    for i in range(i, end):
        arr.append(i)

        print "Numbers now: ", arr
        print "At the bottom i is %d" % i

    print "The arr: "

    for  num in arr:
        print num
print print_for(2, [], 5)
