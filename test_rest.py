from rest import rest

def test_rest():
    assert rest(2, 2) == 0
    assert rest(5, 4) == 1
    assert rest(20, 10) == 10
