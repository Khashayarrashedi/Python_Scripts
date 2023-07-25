#---------------------------------------------- function main
def main():
    time = input("Enter time:  ")
    # time = ("13:00")
    time=convert(time)
    # print(time)

    if 7 <= time <= 8:
        print ("breakfast time")
    elif 12 <= time <= 13:
        print ("lunch time")
    elif 18 <= time <= 19:
        print ("dinner time")


#---------------------------------------------- function convert
def convert(time):
    hour, min = time.split(":")
    min = "{:.2f}".format(float(float(min)/60))
    time=float(int(hour)+float(min))
    return time

#----------------------------------------------  call main
if __name__ == "__main__":
    main()





