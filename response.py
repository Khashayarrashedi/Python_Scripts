from validator_collection import validators, checkers

#-------------------------------------------------------- MAIN
def main():
    email_adress = input("Enter Email: ")
    if checkers.is_email(email_adress) == True:
        print("Valid")
    else:
        print("Invalid")



#-------------------------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()