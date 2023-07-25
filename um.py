import sys
import re


#-------------------------------------------------------- MAIN
def main():
    print(count(input("Text: ")))

#-------------------------------------------------------- FUNC. COUNT
def count(str):
    matches=re.findall(r"\b(um)\b",str, re.IGNORECASE)
    if matches:
        return(len(matches))
    else:
        return None


#-------------------------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()