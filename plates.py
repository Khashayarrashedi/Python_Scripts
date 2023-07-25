import string

def main():
    plate = input("Plate: ")
    # plate="CS05"
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate)<2 or 6<len(plate):
        return False
    elif plate[0] and plate[1] not in string.ascii_uppercase:
        return False
    elif condition_1(plate) == False:
        return False
    else:
        return True

def condition_1(plate):  #if condition is not meet, returns False
    for i in plate:
        if i.isnumeric():
            if i == "0":
                return False
            #check from the first number found until the end of the string
            elif plate[plate.index(i):].isnumeric():
                return True
            else:
                return False
    return True

main()