import sys
from sys import argv
import csv
from tabulate import tabulate

#----------------------------------- MAIN
def main():
    if len(argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")

    match argv[1]:
        case "regular.csv":       #--------------------- CASE REGULAR.CSV
            with open("regular.csv", "r") as file:
                reader=csv.reader(file)
                print(tabulate(reader, headers="firstrow" ,tablefmt="grid"))   #showindex="always"

        case "sicilian.csv":      #--------------------- CASE SICILIAN.CSV
            with open("sicilian.csv", "r") as file:
                reader=csv.reader(file)
                print(tabulate(reader, headers="firstrow" ,tablefmt="grid"))   #showindex="always"

        case _:
            sys.exit("Not a CSV file")

#----------------------------------- MAIN CALL
if __name__ == "__main__":
    main()