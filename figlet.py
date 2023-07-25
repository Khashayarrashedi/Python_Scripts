from pyfiglet import Figlet
import random
import sys

figlet=Figlet()
font_list=figlet.getFonts()                #returns a list of Font

if len(sys.argv) == 3 and sys.argv[2] in font_list and \
    (sys.argv[1]=="-f" or sys.argv[1]=="-font"):
    input_str=input("Enter text: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(input_str))
elif len(sys.argv) ==1:
    input_str=input("Enter text: ")
    random_font=random.sample(font_list, 1)    #pick a random font
    figlet.setFont(font=random_font[0])        #[0] because random_font is a list
    print(figlet.renderText(input_str))
else :
    sys.exit("Invalid usage")