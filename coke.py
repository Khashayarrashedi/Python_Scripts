due=50
while due >0:
    x=int(input("Insert Coin: "))
    # x=5
    match int(x):
        case 5:
            due=due-x
            print(f"Amount Due: {due}" if due>0 else f"Change Owed: {due*-1}")
        case 10:
            due=due-x
            print(f"Amount Due: {due}" if due>0 else f"Change Owed: {due*-1}")
        case 25:
            due=due-x
            print(f"Amount Due: {due}" if due>0 else f"Change Owed: {due*-1}")
        case _:
            print("Amount Due:",due)
# print("Change Owed: ", due if due==0 else "Change Owed: ", due*-1)