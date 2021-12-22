<<<<<<< HEAD
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
=======
<<<<<<< HEAD
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
=======
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
>>>>>>> c67a96dda3fdcc44463f4d331b4703df3b984a5c
>>>>>>> 2927a0e (What's the hell It's working)
