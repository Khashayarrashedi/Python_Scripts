import sys
from sys import argv
import csv
import glob

#######################################   main
def main():
    ref_list, final_list = input_validation(argv)   #---- FUNC. INPUT VALIDATION
    final_list= scourgify(ref_list,final_list)      #---- FUNC. SCOURGIFY

#######################################   FUNC. INPUT VALIDATION
def input_validation(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")

    files_list=glob.glob('*.csv')                       #---- list of csv files in the directory
    if argv[1] in files_list:
        pass
    else:
        sys.exit(f"could not open {argv[1]}")

    return argv[1], argv[2]
#----------------------------------------------------------------------------------------
#----------------------------------------- FUNC. SCOURGIFY ------------------------------
def scourgify(ref_list,final_list):
    headers=["first", "last", "house"]

    try:
        with open(ref_list) as file:
            reader=csv.DictReader(file)
            with open(final_list , 'w') as file1:
                writer=csv.DictWriter(file1, fieldnames=headers)
                writer.writeheader()
                for row in reader:
                    writer.writerow({"first": (row["name"]).split(",")[1].strip(), \
                                     "last": (row["name"]).split(",")[0].strip(), \
                                     "house": row["house"].strip()})
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
#----------------------------------------------------------------------------------------
#----------------------------------------- MAIN CALL -------------------------------------
if __name__ == "__main__":
    main()