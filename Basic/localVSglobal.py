x = 100  # global


def function():
    x = 150  # local
    print('Inside:', x)


function()
print('Outside:', x)


def func():
    y = x+100
    print("Another function:", y)


func()
