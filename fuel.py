def main():
    fuel = get_input("Insert ratio as x/y: ")
    if 0<= fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else :
        print(f"{fuel}%")

def get_input(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            if int(x)>int(y):
                # print(int(x))
                # print(int(y))
                print("Nomerator is bigger than Denomerator. ")
                x=("error")
            if int(x)<0 or int(y)<0:
                print("Numbers must be positive. ")
                x=("error")
            fuel = round(int(x)/int(y)*100)
            return fuel
        except ValueError:
            print("Just Integer, Try again: ")
        except ZeroDivisionError:
            print("Cannot devided by zero, Try again: ")

main()
