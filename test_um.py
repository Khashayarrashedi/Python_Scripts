from um import count


#-------------------------------------------------------- MAIN
def main():
    test_count()
    test_count_1()
    test_count_2()

#-------------------------------------------------------- TEST
def test_count():
    assert count("Um?") == 1
    assert count("um") == 1
    assert count("this is um... CS50.") == 1
    assert count("Um... what") == 1
    assert count("Um, thanks, um, regular expressopns?") == 2

def test_count_1():
    assert count("my name is um, khashy um auma uma aum") == 2
    assert count("Hello, um, world") == 1

def test_count_2():
    assert count("Um? Mum? Is this that album where, um, umm, ") == 2
    assert count("yummy UM, ...Um") == 2

#-------------------------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()