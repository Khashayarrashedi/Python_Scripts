import inflect
import datetime
from datetime import date
import sys


#-------------------------------------------------------- MAIN
def main():
    birthday = input("Enter date: ")
    print(age_minutes(birthday))                    #---- alphabetical show of a number
    # print(alphabetical[0].upper()+alphabetical[1:])           #---- to make the first letter Uppercase

#-------------------------------------------------------- FUNC. AGE MINUTES
def age_minutes(birthday):
    try:
        today= date.today()
        year, month, day=birthday.split("-")                  #---- YYYY-MM-DD
        birthday = datetime.datetime.strptime(birthday,"%Y-%m-%d").date()
        if birthday > today:
            sys.exit("Future date is not possible.")
        elif int(month) < 1 or int(month) > 12:
            sys.exit("Month is out of range.")
        elif int(day) < 1 or int(day) > 31:
            sys.exit("Day is out of range.")

    except ValueError:
        sys.exit("Wrong fromat.")

    #---- till here, the input element is checked and in the right order
    #---- now calculations process

    days=abs((today-birthday).days)
    # print(days)
    minutes=(int(days)*24*60)
    alphabetical = (f"{((inflect.engine()).number_to_words(minutes).replace(' and', ''))} minutes")    #---- alphabetical show of a number
    return (alphabetical[0].upper()+alphabetical[1:])           #---- to make the first letter Uppercase

#-------------------------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()