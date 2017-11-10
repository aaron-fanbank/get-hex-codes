# This code assumes that each image file in the directory contains only
# a single color to be processed and converted into a hex code
import os
from PIL import Image

# Keeps values within the correct range for rgb to hex code coversion
def clamp(x):
    return max(0, min(x, 255))

# Creates new txt file to store the file names and hex codes
outputFileName = raw_input("Enter name for hex code output file: ")
testingFile = open(outputFileName, "w")

# Gets the directory path from user
imageDirectory = raw_input("Enter path to image directroy, or drag and drop: ")

# Removes trailing white space when using a drag and drop method
if imageDirectory.endswith(" "):
    imageDirectory = imageDirectory[:-1]

# Adds the final / to the directory path
imageDirectory = imageDirectory + "/"

# Opens each image in directory, saves separate r,g,b values, then converts
# those values into the correct hexadecimal color code
for filename in os.listdir(imageDirectory):

    # This keeps the code from trying to parse a .DS_Store file
    if not filename.startswith("."):
        im = Image.open(imageDirectory + filename)
        imOpen = im.load()
        a = imOpen[10,10]
        r = a[0]
        g = a[1]
        b = a[2]

        # Gets size of the image
        size = im.size
        # This writes the current filename and converted hex code to the txt
        # file, separated by a tab
        testingFile.write(filename + "\t" + "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b)) + "\r")
    else:
        continue
