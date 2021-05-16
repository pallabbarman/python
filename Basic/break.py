available = 6
n = int(input())
i = 1
while i <= n:
    if i > available:
        print("No available")
        break
    print("Hello")
    i += 1
print("World")
