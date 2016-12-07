def goon(start_value, end_value):
    result = 0
    for i in range(start_value, end_value):
        if i % 3 == 0 or i % 5 ==0:
            if i % 3 == 0 and i % 5 ==0:
                continue
        result += i
    print 'The 3 and 5 result of %i - %i is %i.' % (start_value, end_value, result)

def gen_change(amount):
    boo = amount
    dollars = 0
    quarters = 0
    nickels = 0
    dimes = 0
    pennies = 0

    while amount >= 100:
        dollars+=1
        amount -= 100
    while amount >= 25:
        quarters+=1
        amount -= 25
    while amount >= 10:
        dimes+=1
        amount -= 10
    while amount >= 5:
        nickels+=1
        amount -= 5
    while amount >= 1:
        pennies+=1
        amount -= 1
    print '%i Dollars\n %i Quarters\n %i Dimes\n %i Nickels\n %i Pennies\n\tAre the least amount of coins for %i' % (dollars, quarters, dimes, nickels, pennies, boo)
print goon(3, 333)
print goon(0, 5)
print gen_change(444)
