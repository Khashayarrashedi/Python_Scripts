def main():
    name = input("Please insert your name in Camel Case:   ")
    # name= ("khashyRashedi")
    name=snakecase_name(name)
    print(name)

def snakecase_name(name):
    j = 0
    # sc_name=name
    for i in name:
        if i.isupper():
            name=name[:j]+"_"+name[j:]
            j=j+1
            name=name.lower()
        j=j+1
    return name

main()