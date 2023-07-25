##############################################################################
##########################      BMI INDEX CALCULATOR     #####################
##############################################################################
'''
Brief Description:
    The function of this project is to calculate the Body Mass Index (BMI) of
    the users and show them a graphical expression of their health status.
    BIM is calculated by deviding weight in kilograms by height squared in Meters.

    This application shows result in 4 different ranges:
    1. underweight shown in yellow (below 18.5)
    2.  healthy weight shown in green (18.5 to 24.9)
    3. overweight shown in yellow (25 to 29.9)
    4. obese shown in red (30 or over)
'''
##############################################################################
from termcolor import colored

#------------------------------------------------------- MAIN
def main():
    name, height, weight = get_input()
    BIM_index= BIM_calculator(height, weight)
    graphical_view(name, BIM_index)

#------------------------------------------------------- FUNCTION GET_NAME
def get_input():
    name = input("Enter your Name: ")
    while True:
        try:
            height = int(input("Enter your height in centimeter: "))
            break
        except ValueError:
            print("Your input is not in a proper range. /n Please Enter your height in centimeter:")
            pass
    while True:
        try:
            weight = int(input("Enter your weight in kilogram: "))
            break
        except ValueError:
            print("Your input is not in a proper range. \nPlease Enter your weight in kilogram:")
            pass

    return name, height, weight

#------------------------------------------------------- FUNCTION BIM_CALCULATOR
def BIM_calculator(height, weight):
    BIM_index = round(weight/(height/100)**2, 2)
    return BIM_index


#------------------------------------------------------- FUNCTION GRAPHICAL VIEW
def graphical_view(name, BIM_index):
    area_1= "|------------"
    area_2= "18.5------------24.9"
    area_3= "----------29.9"
    area_4= "------------|"

    if BIM_index < 18.5:
        print(f"\n Dear {name},\nWatch your health.\n Your BIM index is {BIM_index:.2f} categorised as Underweight. \n\n")
                    # |------------18.5------------24.9----------29.9------------|
        print(colored(f"     {BIM_index:.2f}", "yellow"))
    elif 18.5 <= BIM_index <= 24.9:
        print(f"\n Dear {name},\n Congratulations.\n Your BIM index is {BIM_index:.2f} categorised as Normal. \n\n")
                    # |------------18.5------------24.9----------29.9------------|
        print(colored(f"                    {BIM_index:.2f}", "green"))
    elif 24.9 < BIM_index <= 29.9:
        print(f"\n Dear {name},\nWatch your health.\n Your BIM index is {BIM_index:.2f} categorised as Overweight. \n\n")
                    # |------------18.5------------24.9----------29.9------------|
        print(colored(f"                                   {BIM_index:.2f}", "yellow"))
    elif 29.9 < BIM_index :
        print(f"\n Dear {name},\n You need an immediate action.\n Your BIM index is {BIM_index:.2f} categorised as Obese. \n\n")
                    # |------------18.5------------24.9----------29.9------------|
        print(colored(f"                                                   {BIM_index:.2f}", "red"))


    print (colored( area_1 , "yellow")+ colored( area_2 , "green") + colored( area_3 , "yellow") + colored( area_4 , "red"))
    print (colored( "|UNDERWEIGHT        " , "yellow")+ colored("NORMAL        ", "green") + colored("OVERWEIGHT       ", "yellow") + colored("OBESE   |", "red")+"\n\n")



#------------------------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()