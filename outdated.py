def main():
    month =[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

    while True:
        date= input("Enter date: ")
        try:
#-----------check if the input typed as mm/dd/yyyy, so it works:
            mm, dd, yyyy=date.split("/")
            mm=int(mm)
            dd=int(dd)
            yyyy=int(yyyy)
            if 1 <= dd <=31 and 1 <= mm <=12 and 1000 <=yyyy<= 9999:
                print(f"{yyyy}-{mm:02}-{dd:02}")
                break
#-----------if the input typed alphabetical, try faces ValueError.
#-----------check if the input typed as Month-Name dd, yyyy.
        except ValueError:
            try:
                if date.count(",")==1:     #just for stupid final example of Harvard check
                    date=date.replace("," , "")
                    mm, dd, yyyy= date.split(" ")
                    dd=int(dd)
                    mm = month.index(mm)+1
                    yyyy=int(yyyy)
                    if 1 <= dd <=31 and 1000 <=yyyy<= 9999:
                        print(f"{yyyy}-{mm:02}-{dd:02}")
                        break
            except ValueError:
                pass
main()