## StdAlgors.py
##
## Written by Matthew Egan
## Written on 3rd Apr 2013
## Subroutines for all std algorithms refered to
## by the NSW HSC SDD Course Specs (Section 7)

# Load an array and print its contents
# Given an array print its contents
def printArr(arrayToPrint):
    for i in arrayToPrint:
        print i,

# Add the contents of an array of numbers
# Given an array, return the total sum
def addArr(arrayToAdd):
    total = 0
    for number in arrayToAdd:
        total += number
    return total

# Finding the maximum value in an array
# Given an array, return the max value
def maxOfArr(arrayToSearch):
    maximum = 0
    for i in arrayToSearch:
        if i > maximum:
            maximum = i
    return maximum

# Finding the minimum value in an array
# Given an array, return the min value
def minOfArr(arrayToSearch):
    minimum = arrayToSearch[0]
    for index in len(arrayToSearch):
        if arrayToSearch[index] < minimum:
            minimum = arrayToSearch[index]
    return minimum

# Extracting data from a string
# Given a string, remove a portion from a to b
def extractFromString(extractionString, a, b):
    return extractionString[a:b]

# Insertion of a string into another string
# Given a string, insert another string
def insertString(mainString, stringToInsert, pos):
    preString = mainString[:pos]
    posString = mainString[pos:]
    newString = preString + stringToInsert + posString
    return newString

# Deletion of a string from another string
# Given a string, delete an internal string from a to b
def deleteWithinString(mainString, a, b):
    preString = mainString[:a]
    posString = mainString[b:]
    newString = preString + posString
    return newString

# Generate a set of unique random numbers
# Implements the middle-square method
# en.wikipedia.org/wiki/Pseudo-random_number_generator
def makeRandSet(seed, numsToGenerate):
    arrayOfRandoms = []
    for iterations in xrange(numsToGenerate + 1):
        seed = seed*seed
        lenSides = len(str(seed))/4
        seed = seed[lenSides:-lenSides]
        arrayOfRandoms.append(seed)
    return arrayOfRandoms

# Create a file
# Given a filename, create a txt document
def createAFile(filename):
    return open(str(filename)+".txt", "r+a")

# Print the contents of a file
# Given a file, print the contents down the page
def printFile(filename):
    for line in filename:
        print line

# Appending records to an existing seq file
# Given a file, append a string
def appendToFile(filename, stringToAppend):
    for line in filename:
        if line == None:
            filename.write(stringToAppend)



