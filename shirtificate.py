from fpdf import FPDF
from PIL import Image



#------------------------------------------------------ MAIN
def main():
    name= input("Fullname :")

    pdf= FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "", 20)
    pdf.set_text_color(255,255,0)
    pdf.write(txt= f"{name} took CS50")
    pdf.output("shirtificate.pdf")










#----------------------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()