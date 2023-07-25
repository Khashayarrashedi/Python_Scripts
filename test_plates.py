from plates import is_valid

#------------------------------- MAIN DEFINE
def main():
    test_1()     #---- correctness
    test_2()     #---- first 2 character
    test_3()     #---- first 2 character
    test_4()     #---- no alphabet after numbers
    test_5()     #---- string lenght
    test_6()     #---- Puntuation
    test_7()     #---- zero placement

#------------------------------- TEST DEFINITIONS
def test_1():     #---- correctness
    assert is_valid("AAB250") == True

def test_2():     #---- first 2 character
    assert is_valid("A2B555") == False

def test_3():     #---- first 2 character
    assert is_valid("25") == False

def test_4():     #---- no alphabet after numbers
    assert is_valid("SS250A") == False

def test_5():     #---- string lenght
    assert is_valid("AAAAAAAA") == False

def test_6():     #---- Puntuation
    assert is_valid("AA21.A") == False

def test_7():     #---- zero placement
    assert is_valid("AA025") == False

#------------------------------- MAIN CALL
if __name__ == "__main__":
    main()