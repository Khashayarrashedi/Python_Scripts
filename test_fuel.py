from fuel import convert, gauge
import pytest

#------------------------------- MAIN
def main():
    test_convert()
    test_gauge()

#------------------------------- CONVERT FUNC. TESTS
def test_convert():
    assert convert("2/5") == 40                #---- correctness
    # assert convert("1/0") is ZeroDividionError
    with pytest.raises(ZeroDivisionError):     #---- zero division test
        convert("1/0")
    with pytest.raises(ValueError):            #---- more than 100%
        convert("5/2")
    with pytest.raises(ValueError):            #---- less than 0%
        convert("-2")
    with pytest.raises(ValueError):            #---- less than 0%
        convert("-2/-4")
    with pytest.raises(ValueError):            #---- less than 0%
        convert("2/-4")
#------------------------------- GAUGE FUNC. TESTS
def test_gauge():
    assert gauge(99) == "F"                    #---- full gauge
    assert gauge(1) == "E"                     #---- empty gauge
    assert gauge(20) == "20%"                  #---- ordinary gauge

#------------------------------- MAIN CALL
if __name__ == "__main__":
    main()