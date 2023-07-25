
#---------------------------------------------- inputs
input_var = input("Enter:   ")
input_var=input_var.lower().strip()

#---------------------------------------------- program blackbox
match input_var:
    case "42" | "forty two" | "forty-two" :
        print ("Yes")
    case _ :
        print ("No")