
#---------------------------------------------- Inputs
input_str = input("Enter file name:   ")
input_str = input_str.lower().strip()

# input_str= ("  aaa.jp ")
# input_str = input_str.lower().strip()
#---------------------------------------------- BlackBox
import re     #---- to use re.search()   --> the output is True of False
                #^The: starts with "The"
                #. any charachters
                #The$ ends with "The"
                #* zero or more accurance (char)
                #+ one or more accurance (char)
                #He.{2}o : exactly 2 char in between (any char)
                #[a-e-r-3] :a set of char

if re.search(".gif$", input_str):
    print ("image/gif")
elif re.search(".jpg$", input_str):
    print ("image/jpeg")
elif re.search(".png$", input_str):
    print ("image/png")
elif re.search(".txt$", input_str):
    print ("text/plain")
elif re.search(".pdf$", input_str):
    print ("application/pdf")
elif re.search(".zip$", input_str):
    print ("application/zip")
elif re.search(".jpeg$", input_str):
    print ("image/jpeg")
else:
    print ("application/octet-stream")
