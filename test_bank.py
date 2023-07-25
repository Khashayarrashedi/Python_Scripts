from bank import value

def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert value("hello") == 0 #"$0"

def test_2():
    assert value("Hi") == 20 #"$20"

def test_3():
    assert value("whats up") == 100 #"$100"
    assert value("123") == 100 #"$100"

if __name__ == "__main()__":
    main()