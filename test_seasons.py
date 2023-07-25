import seasons
from seasons import age_minutes

def main():
    test_1()


def test_1():
    assert age_minutes("2022-06-25") == "Five hundred twenty-five thousand, six hundred minutes"



if __name__ == "__main__":
    main()