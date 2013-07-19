## alphashift.py
##
## Written by Matthew Egan
## Written on 18th July 2013
##
## Given an integer, shift the alphabet
## Given 2 => A -> C, B -> D

def main():
	name = raw_input("Enter string: ")
	shifted = alphashift(2)
	for letter in name:
		print shifted[letter],

def alphashift(shiftVal):
    import string
    alphabet = string.lowercase
    alphaDict = {}
    for character in alphabet:
        alphaDict[character] = alphabet[(alphabet.index(character) + shiftVal) % 26]
    return alphaDict

if __name__ == "__main__": main()