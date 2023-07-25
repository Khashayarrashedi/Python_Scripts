import sys
import re


#-------------------------------------------------------- MAIN
def main():
    print(convert(input("Hours: ")))           #---- pattern: 9:00 AM to 10:00 PM
                                               #---- or       9 AM to 10 PM


#-------------------------------------------------------- FUNC. CONVERT
def convert(str):
    if matches := re.search(r"(10|11|12|[0-9]):?([0-9]|[0-5][0-9])? (AM|PM) to (10|11|12|[0-9]):?([0-9]|[0-5][0-9])? (AM|PM)", str):
        #---- above line result for input 10 AM to 12 PM: ('10', None, 'AM', '12', None, 'PM')


        if matches.group(3)=="AM":              #---- start time
            start_hour=int(matches.group(1))
            if start_hour == 12:
                start_hour=0
        else:
            start_hour=int(matches.group(1))+12
            if start_hour == 24:
                start_hour=12

        if matches.group(2)== None:
            start_min="00"
        else:
            start_min=matches.group(2)

        if matches.group(6)=="AM":              #---- end time
            end_hour=int(matches.group(4))
            if end_hour == 12:
                end_hour=0
        else:
            end_hour=int(matches.group(4))+12
            if end_hour == 24:
                end_hour=12

        if matches.group(5)== None:
            end_min="00"
        else:
            end_min=matches.group(5)

    else:
        raise ValueError


    return (f"{start_hour:02}:{start_min} to {end_hour:02}:{end_min}")



#-------------------------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()