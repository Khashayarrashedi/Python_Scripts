from random import randint

def main():
    level=get_level()
    correct_ans= 0

    for i in range(10):        #------ generating 10 questions
        x , y=generate_integer(level)
        print(f"{x} + {y} = ")

        for c in range(1,4):      #------- user ans iteration counter (Max=3)
            try:
                if int(input()) == x+y:    #----- input is the user ans
                    correct_ans = correct_ans +1
                    break
                else:
                    print("EEE") if c != 3 else 0
                    print(f"{x} + {y} = {x+y}") if c==3 else 0
            except ValueError:
                    pass


    # ------- printing score and finish
    print("score: " ,correct_ans)



def get_level():       #----------- just get level from user
    while True:
        try:
            level=int(input("Enter Level 1, 2 or 3: "))
        except ValueError:
            pass
        else:
            if 1 <= level <=3:
                return level
            else:
                pass


def generate_integer(level):    #-------------- generate two random numbers
    if level == 1:
        x = randint(0 ,9)
        y = randint(0 ,9)
    elif level ==2:
        x = randint(10 ,99)
        y = randint(10 ,99)
    else:
        x = randint(100 ,999)
        y = randint(100 ,999)
    return x , y


if __name__ == "__main__":
    main()