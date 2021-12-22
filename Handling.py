# This Python program is use to write data to file.
def WriteData(FileName,Data):
    with open(FileName,"a+") as fOut:
        fOut.write(Data + "\n")

WriteData("Main.txt","My program is Running...")        


# ////////////////////////////////////////////////////////////////#

# Python program to create a new file in another directory.
import os

def AddFile(FileName,Path):
    filename = FileName
    Route = Path
    Fullintro = os.path.join(Route, filename)
    open(Fullintro, "w")


AddFile("Mozilla.txt","C:\\Users\\dna83\\OneDrive\\Desktop\\Your dad") 


# ////////////////////////////////////////////////////////////////#

# Append content to a file in Python.

def AppendContents(filename, content):
    file = open(filename, "a+")
    file.write(content)
    file.close()

AppendContents("Main.txt","My Append Content program is working......")    

# /////////////////////////////////////////////////////////////////#

# Read contents of the file using readline() method in Python.
def Read(filename):
    file = open(filename + ".txt","r") 
    data = file.readline()
    while data:
        print(data)
        data = file.readline()
    file.close()


Read("Main.txt",)        

# /////////////////////////////////////////////////////////////////#

# Read contents of a file using readline() method and manipulating it in Python
def Manipulation(filename):
    file = open(filename + ".txt","r")
    data = len(file.readlines())
    while data:
        print(data)
        data = len(file.readline())

Manipulation("Main.txt")
 
# /////////////////////////////////////////////////////////////////#

# Copy contents from one file to another file in Python.

def CopyPaste(copyfilename,pastefilename):
    with open(copyfilename) as fObj:
        data = fObj.read()

    with open(pastefilename,"a+") as fObj:
        fObj.write(data)
        print(f"I have Copy data from {copyfilename} and pasted to {pastefilename}.")

CopyPaste("Main.txt","hello.txt")

# /////////////////////////////////////////////////////////////////#

# Copy odd lines of one file to another file in Python

def CopyPasteOddLines(copyfilename,pastefilename):
    copyfile = open(copyfilename, "r+")
    pastefile= open(pastefilename, "w+")
    count = copyfile.readlines()
    for i in range(0,len(count)):
        if(i % 2 == 0):
            pastefile.write(count[i])
        else:
            pass


    pastefile.close()
    pastefile = open(pastefilename, "r")
    count1 = pastefile.read()
    print(count1)

CopyPasteOddLines("hello.txt", "Main.txt")    

# This Python program is use to write data to file.
def WriteData(FileName,Data):
    with open(FileName,"a+") as fOut:
        fOut.write(Data + "\n")

WriteData("Main.txt","My program is Running...")        


# ////////////////////////////////////////////////////////////////#

# Python program to create a new file in another directory.
import os

def AddFile(FileName,Path):
    filename = FileName
    Route = Path
    Fullintro = os.path.join(Route, filename)
    open(Fullintro, "w")


AddFile("Mozilla.txt","C:\\Users\\dna83\\OneDrive\\Desktop\\Your dad") 


# ////////////////////////////////////////////////////////////////#

# Append content to a file in Python.

def AppendContents(filename, content):
    file = open(filename, "a+")
    file.write(content)
    file.close()

AppendContents("Main.txt","My Append Content program is working......")    

# /////////////////////////////////////////////////////////////////#

# Read contents of the file using readline() method in Python.
def Read(filename):
    with open(filename) as fObj:
        data = fObj.read()
        print(data)


Read("Main.txt",)        

# /////////////////////////////////////////////////////////////////#

# Read contents of a file using readline() method and manipulating it in Python
def Manipulation(filename):
    with open(filename) as fObj:
        data = fObj.read()
        print(data)
        print(f"Number of Characters in {filename} " + str(len(data)))

Manipulation("Main.txt")
 
# /////////////////////////////////////////////////////////////////#

# Copy contents from one file to another file in Python.

def CopyPaste(copyfilename,pastefilename):
    with open(copyfilename) as fObj:
        data = fObj.read()

    with open(pastefilename,"a+") as fObj:
        fObj.write(data)
        print(f"I have Copy data from {copyfilename} and pasted to {pastefilename}.")

CopyPaste("Main.txt","hello.txt")

# /////////////////////////////////////////////////////////////////#

# Copy odd lines of one file to another file in Python

def CopyPasteOddLines(copyfilename,pastefilename):
    copyfile = open(copyfilename, "r+")
    pastefile= open(pastefilename, "w+")
    count = copyfile.readlines()
    for i in range(0,len(count)):
        if(i % 2 == 0):
            pastefile.write(count[i])
        else:
            pass


    pastefile.close()
    pastefile = open(pastefilename, "r")
    count1 = pastefile.read()
    print(count1)

CopyPasteOddLines("hello.txt", "Main.txt")    

# This Python program is use to write data to file.
def WriteData(FileName,Data):
    with open(FileName,"a+") as fOut:
        fOut.write(Data + "\n")

WriteData("Main.txt","My program is Running...")        


# ////////////////////////////////////////////////////////////////#

# Python program to create a new file in another directory.
import os

def AddFile(FileName,Path):
    filename = FileName
    Route = Path
    Fullintro = os.path.join(Route, filename)
    open(Fullintro, "w")


AddFile("Mozilla.txt","C:\\Users\\dna83\\OneDrive\\Desktop\\Your dad") 


# ////////////////////////////////////////////////////////////////#

# Append content to a file in Python.

def AppendContents(filename, content):
    file = open(filename, "a+")
    file.write(content)
    file.close()

AppendContents("Main.txt","My Append Content program is working......")    

# /////////////////////////////////////////////////////////////////#

# Read contents of the file using readline() method in Python.
def Read(filename):
    with open(filename) as fObj:
        data = fObj.read()
        print(data)


Read("Main.txt",)        

# /////////////////////////////////////////////////////////////////#

# Read contents of a file using readline() method and manipulating it in Python
def Manipulation(filename):
    with open(filename) as fObj:
        data = fObj.read()
        print(data)
        print(f"Number of Characters in {filename} " + str(len(data)))

Manipulation("Main.txt")
 
# /////////////////////////////////////////////////////////////////#

# Copy contents from one file to another file in Python.

def CopyPaste(copyfilename,pastefilename):
    with open(copyfilename) as fObj:
        data = fObj.read()

    with open(pastefilename,"a+") as fObj:
        fObj.write(data)
        print(f"I have Copy data from {copyfilename} and pasted to {pastefilename}.")

CopyPaste("Main.txt","hello.txt")

# /////////////////////////////////////////////////////////////////#

# Copy odd lines of one file to another file in Python

def CopyPasteOddLines(copyfilename,pastefilename):
    copyfile = open(copyfilename, "r+")
    pastefile= open(pastefilename, "w+")
    count = copyfile.readlines()
    for i in range(0,len(count)):
        if(i % 2 == 0):
            pastefile.write(count[i])
        else:
            pass


    pastefile.close()
    pastefile = open(pastefilename, "r")
    count1 = pastefile.read()
    print(count1)

CopyPasteOddLines("hello.txt", "Main.txt")    

#//////////////////////////////////////////////////////////////////#

# Count the total number of uppercase characters in a file in Python

def TotalUppercase(Filename):
    file = open(Filename, "r")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count+=1
    print(count)
    file.close()

TotalUppercase("Main.txt") 

# //////////////////////////////////////////////////////////////////#

# Python program to count total number of uppercase and lowercase characters in file




def TotalUpperAndLowercase(Filename):
    file = open(Filename, "r")
    data = file.read()
    countup = 0
    countlo = 0
    for letter in data:
        if letter.isupper():
            countup+=1
        elif letter.islower():
            countlo+=1   
    print(countup + countlo)
    file.close()


TotalUppercase("Main.txt")  

# //////////////////////////////////////////////////////////////////#

# Python program to delay printing of lines from a file using sleep function

import time

def TimeDelay(FileName):
    file =  open(FileName,"r")
    while(True):
            File = file.read(1)
            if (File == ""):
                break
            print(File, end = "")
            time.sleep(0.50)
    file.close()


TimeDelay("MySelf.txt")

#///////////////////////////////////////////////////////////////////#

# Python program to count the number of lines in a file

def Linecount(filename):
    file = open(filename + '.txt', 'r')
    Counter = 0
    Read = file.read()
    countlist = Read.split('\n')
    for i in countlist:
        if i :
            Counter += 1
    print(f"Number of Lines In {filename} is " + str(Counter))

Linecount("MySelf")

#///////////////////////////////////////////////////////////////////#

# Python program to check a file's status in file Handling

def status(filename):
    file = open(filename + ".txt", 'rb')
    FileName = file.name
    Fileclosedoropen = file.closed
    FileMode = file.mode
    print(FileName)
    print(Fileclosedoropen)
    print(FileMode)
    file.close()

    Fileclosedoropen = file.closed
    print("")
    print(Fileclosedoropen)
    
status("MySelf") 

#///////////////////////////////////////////////////////////////////#

# Python program to delete a file

import os
def delete(filename):
    os.remove(filename)
    print(f"{filename} is deleted")

delete(".txt")









