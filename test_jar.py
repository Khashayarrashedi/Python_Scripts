from jar import Jar
# from Jar import *
# from jar import *

def test_init():
    # jar=Jar()
    # assert jar.capacity() == 12
    # jar_2 = Jar(10)
    # assert jar_2.capacity() == 10
    jar_3 = Jar(15)
    assert jar_3.__init__() == None


def test_str():
    jar=Jar()
    jar.deposit(2)
    assert jar.__str__() == "🍪🍪"
    jar.deposit(3)
    assert jar.__str__() == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    assert jar.deposit(6) == None      #---- it is 6 but nothing should be returned


def test_withdraw():
    jar=Jar()
    jar.deposit(5)
    assert jar.withdraw(2) == None      #---- it is 3 but nothing should be returned

# def test_capacity():
#     jar=Jar()
#     jar.deposit(5)
#     assert jar.capacity() == 7

# def test_size():
#     jar=Jar()
#     jar.deposit(5)
#     assert jar.size() == 5
