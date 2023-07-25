from working import convert
import pytest

#-------------------------------------------------------- MAIN
def main():
    test_1()


#-------------------------------------------------------- TESTS
def test_1():
    assert convert("9:00 AM to 10 PM") == "09:00 to 22:00"
    assert convert("8 AM to 12 PM") == "08:00 to 12:00"

def test_2():
    with pytest.raises(ValueError):
        convert("8 AM 12 PM")

def test_3():
    with pytest.raises(ValueError):
        convert("25 AM to 12 PM")


#-------------------------------------------------------- MAIN
if __name__ == "__main__":
    main()