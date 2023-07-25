import os
import os.path
import glob
import sys
from sys import argv
import PIL
from PIL import Image, ImageOps

#----------------------------------------- MAIN
def main():
    before, after =input_validation(argv)             #---- if constrains are desired, return the file name
    print(before)
    print(after)

    img_2= Image.open("shirt.png")                    #---- image to be paste and mask the BG
    size=img_2.size

    bg_img= Image.open(before)                        #---- background image
    bg_img = ImageOps.fit(bg_img, (size[0], size[1])) #, method = 0, bleed = 0.0, centering =(0.5, 0.5)
    bg_img.paste(img_2,img_2)
    bg_img.save(after)



#---------------------------------------- FUNC. INPUT_VALIDATION
def input_validation(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.splitext(argv[1])[1] not in [".jpg",".jpeg",".png"]:       #---- .ext of 1st file
        sys.exit("Invalid output 1")
    elif os.path.splitext(argv[2])[1] not in [".jpg",".jpeg",".png"]:       #---- .ext of 2nd file
        sys.exit("Invalid output 2")
    elif os.path.splitext(argv[1])[1] != os.path.splitext(argv[2])[1]:  #---- check .ext of both files' equality
        sys.exit("Input and output have different extentions")
    #---- till here, number of imputs and extentions are valid, then lets' check file existence

    files_list=glob.glob('*')                    #---- list of files in the directory
    if argv[1] in files_list:
        pass
    else:
        sys.exit("Input does not exist")

    return argv[1], argv[2]


#---------------------------------------- FUNC.





#----------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()






# # Importing Image and ImageOps module from PIL package
# from PIL import Image, ImageOps

# # creating a image1 object
# im1 = Image.open("before1.jpg")

# # applying fit method
# # Setting width = 100 and height = 100
# im2 = ImageOps.fit(im1, (600, 600)) #, method = 0, bleed = 0.0, centering =(10, 10)

# im2.save("after.jpg")

# # Image.show("after.jpg")
