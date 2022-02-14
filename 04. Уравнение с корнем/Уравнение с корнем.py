a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print('NO SOLUTION')

elif (a + b) == c**2 and (3 * a + b) == c**2:
    print('MANY SOLUTIONS')

else:
    if a != 0 and (c * c - b) / a == (c * c - b) // a:
        print((c * c - b) // a)
    else:
        print('NO SOLUTION')