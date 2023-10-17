a = 10  # Global Variable
b = 20


def test_local_global():
    print("Inside func Global", globals()['a'])
    globals()['a'] = 15
    a = 5  # Local Variable
    print("Inside func local", a)
    a = 25
    print("Inside func local", a)


b = b + 1
test_local_global()
print("Outside func", a)
print("b=", b)
