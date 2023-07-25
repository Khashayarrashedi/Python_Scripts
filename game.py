import random

def main():
    while True:
        try:
            n=int(input("Level:"))
        except ValueError:
            pass
        else:
            if n >0:
                ans=random.randint(1,n)
                break
    while True:
        try:
            guess=int(input("Guess:"))
        except ValueError:
            pass
        else:
            if guess < 1 or guess > n:
                pass
            elif guess > ans:
                print("Too large!")
            elif guess < ans:
                print("Too small!")
            else:
                print("Just right!")
                break

if __name__ == '__main__':
    main()