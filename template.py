## template.py
##
## Template written by Matthew Egan
## Template written on 19th July 2013
##
## Written by <team name>
## Written on 19th July 2013
##
## UNSW ProgComp Question: 0

def main():
    array = [1,2,3]
    writeArrayToFile("test.txt", array)

def loadFile(filename):
    return open(filename, "rU")

def loadFileInArray(filename):
    f = open(filename, "rU")
    array = [line for line in f]
    f.close()
    return array

def writeArrayToFile(filename, array):
    f = open(filename, "w")
    for item in array:
        f.write(str(item) + "\n")
    f.close()

if __name__ == "__main__": main()