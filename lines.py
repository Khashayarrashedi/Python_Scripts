import sys
from sys import argv
import glob


#----------------------------------------- MAIN
def main():
    file_name =input_validation(argv)             #---- if constrains are desired, return the file name
    edited_file=file_modification(file_name)      #---- trimming the file in a requested way
    print(len(edited_file))                       #---- printing the result


#---------------------------------------- FUNC. FILE_MODIFICATION
def file_modification(file_name):
    edited_file=[]
    with open(file_name) as file:
        for line in file:
            if line.lstrip().startswith("#"):           #--- removing comment lines
                del line
            elif len(line.strip())==0:                  #--- removing empty lines
                del line
            elif line.lstrip().startswith("\'\'\'"):    #--- removing docstring lines
                del line
            else:
                edited_file.append(line)
    return(edited_file)

#---------------------------------------- FUNC. INPUT_VALIDATION
def input_validation(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")
    elif argv[1].endswith(".py"):
        pass
    else :
        sys.exit("Not a python file")

    files_list=glob.glob("*.py")          #---- list of .py files in the directory

    if argv[1] in files_list:
        pass
    else:
        sys.exit("File does not exist")

    return argv[1]


#----------------------------------- MAIN CALL
if __name__ == "__main__":
    main()