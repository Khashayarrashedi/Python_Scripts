from numb3rs import validate

#-------------------------------------------------------- MAIN
def main():
    test_1()


#-------------------------------------------------------- TESTS
def test_1():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("a.0.0.0") == False
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.256") == False
    assert validate("300.0.0.0") == False
    assert validate("cat") == False
    assert validate("0.0.0.") == False
    assert validate("0.0.0") == False

#-------------------------------------------------------- MAIN
if __name__ == "__main__":
    main()