import inflect
p=inflect.engine()

def main():
    names=[]
    while True:
        try:
            names.append(input())  #making a list of names of user input
        except EOFError:
            break

    print("Adieu, adieu, to "+ p.join(names)) #see inflect p.join feature

main()