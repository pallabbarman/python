x = int(input("Enter number: "))
if x < 0:
    print('x is negative')
else:
    print('x is positive')
    if(x % 2) == 0:
        print('Number is even')
    else:
        print('Number is odd')
