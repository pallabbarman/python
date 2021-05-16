num = int(input())
for i in range(2, num):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("Number is prime")
