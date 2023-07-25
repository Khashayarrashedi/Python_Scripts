from twttr import shorten

def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert shorten("khashayar") == "khshyr"

#--------------- TEST FOR CAPITALIZED VOWEL
def test_2():
    assert shorten("KHASHAYAR") == "KHSHYR"

#--------------- TEST FOR OMITTING NUMBERS AND PUNCTUATION
def test_3():
    assert shorten("kho1.") == "kh1."

if __name__ == "__main__":
    main()