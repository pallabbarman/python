def add(a, b):
    # normal argument
    c = a+b
    print(c)


add(6, 9)


def mul(*num):
    # non keyword argument *args
    c = 1
    for i in num:
        c *= i
    print(c)


mul(2, 5, 6, 9)


def myself(age, **others):
    # keyword argument **kwargs
    print(age)
    print(others)


myself(23, name="Pallab", varsity="BUBT", country="BD")
