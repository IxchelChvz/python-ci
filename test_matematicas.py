from matematicas import add, mul, rest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10, 20) == 30

def test_multiply():
    assert mul(2,2) == 4
    assert mul(5,5) == 25

def test_rest():
    assert rest(10, 5) == 5

test_multiply()
test_add()
test_rest()