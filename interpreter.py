
#---------------------------------------------- Inputs
input_str = input ("Enter you equaltion:    ")
# input_str =("2.22 / 3")

#---------------------------------------------- Black Box
x, sym, y = input_str.split(" ")    #sym= mathematical symbol + - * /

if sym=="+" :
    print ("{:.1f}".format(float(x)+float(y)))
elif sym=="-" :
    print ("{:.1f}".format(float(x)-float(y)))
elif sym=="*" :
    print ("{:.1f}".format(float(x)*float(y)))
elif sym=="/" :
    print ("{:.1f}".format(float(x)/float(y)))




