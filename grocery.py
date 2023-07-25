def main():
    grocery_list = {}
    while True:
            item = get_item(grocery_list)
            if item in grocery_list:
                grocery_list[item]= int(grocery_list[item])+1
            else:
                grocery_list[item]=1

def get_item(grocery_list):
    try:
        return (input().upper())
    except EOFError:
        list=sorted(grocery_list)
        for i in list:
            print(f"{grocery_list[i]} {i}")
        exit()

main()