
#---------------------------------------------- Inputs
input_str = input("Enter you greeting sentence:   ")

#---------------------------------------------- BlackBox
input_str=input_str.lower().strip()

if input_str[:5]== "hello":
        print("$0")
elif input_str[:1] == "h":
        print("$20")
else :
       print("$100")