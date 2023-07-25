import sys
import re


#-------------------------------------------------------- MAIN
def main():
    print(parse(input("HTML: ")))

#-------------------------------------------------------- FUNC. WATCH
def parse(str):
    matches = re.search(r"https?://(?:www.)?youtube.com/embed/(.+)\"",str, re.IGNORECASE)
    if matches:
        return (f"https://youtu.be/{matches.group(1)}")

#-------------------------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()