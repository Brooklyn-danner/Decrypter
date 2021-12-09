# Feel free to start from scratch, or repurpouse any of these suggested functions! The world is yours. 
#   Well, maybe that was a bit of an over exaggeration. The world isn't only *yours*, but this text file sure is. 

import sys
import os

def sendError(string=""):
    '''
Exits the program after displaying `string` as an error message. If no string
input is provided, the default message is "Error! An error was encountered, so
the program is quitting."
    '''
    # Dear Future Dev,
    # The code below is fine. Your work is not needed on `sendError`.
    # You are more than welcome to edit the string literal, especially to make
    # a more vocal and unique quack.
    if string == "":
        string = "Error! An error was encountered, so the program is quitting."
    print(f"""\
!!!QUACK!!!
================================================================================
{string}
================================================================================
!!!QUACK!!!
""")
    sys.exit(1)



#makes sure we can open the file safely. send error if not
def getFileSafe(path):
    if (os.access(path,os.R_OK)) :
        p = open(path)
        return p
    if not (os.access(path,os.R_OK)) :
        sendError()


#loops through file and translates line by line
def incr(file):
    newOne=""
    for i in file.readlines() :
        newOne= newOne + decryptLine(i)
    return newOne


#translates the flag and character code into its respective letter or symbol
#ord converts a character into its unicode
#chr takes ASCII value and outputs string
def translate(char):
    if char[0]== '^':
        char=char[1:]
        return chr(65 + int(char))
    elif char[0]== '_':
        char=char[1:]
        return chr(97 + int(char))
    elif char[0]== '+':
        char = char[1:]
        if char[0] == "A":
            return chr(32 + int(char[1:]))
        elif char[0] == "B":
            return chr(91 + int(char[1:]))
        elif char[0] == "C":
            return chr(123 + int(char[1:]))


#call decrypt character to decrypt the characters in the line. loop until you see another flag.
def decryptLine(line):
    output= ""
    arr = line.split()
    #loop through the line
    for i in arr:
        output = output + translate(i)
    return output


if __name__ == '__main__':
    filename = input("What is the file you want to read? ")
    file = getFileSafe(filename)
    print(incr(file))

    file.close()



