from project import BIM_calculator
from project import graphical_view


def test_BIM_calculator_1():
    assert BIM_calculator(170,90) == 31.14
    assert BIM_calculator(150,50) == 22.22

def test_BIM_calculator_2():
    assert BIM_calculator(190,70) == 19.39

def test_BIM_calculator_3():
    assert BIM_calculator(160,60) == 23.44

def test_BIM_calculator_4():
    assert graphical_view("Khashayar", 25) == None
    assert graphical_view("Rashedi", 12.215) == None
    assert graphical_view("Khashayar", 0) == None