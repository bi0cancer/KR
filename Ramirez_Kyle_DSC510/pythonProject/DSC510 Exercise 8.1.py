# Week 9
# 9.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 15-May-2021
# Assignment is to create a program that will:
# Open the file and process each line.
# Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
# Nicely print the output, in this case from high to low frequency.
# Create a new function called process_fie. This function will perform the same operations as
# pretty_print from week 8 however it will print to a file instead of to the screen.

wordList = list()
wordDic = {}


# function that processes the each line of the file and appends to the word list
def processLine(gba_file):
    for line in gba_file:
        for word in line.split():
            wordList.append(word)
    return wordList


# calculates how many of each word there is within the word list
def addWord():
    for word in wordList:
        if word in wordDic:
            wordDic[word] += 1
        else:
            wordDic[word] = 1
    return wordDic


# prints the number of words in the file, gives it a header, and prints the dictionary keys and values
def prettyPrint(wordDic):
    print("Number of words in the file is: ", len(wordList))
    print("Word", "Count")
    for key, value in wordDic.items():
        print(key, value)


# main will call each function in the proper order in order to print the number of words in the file
# a header, and the keys within the dictionary along with the number of times those words repeat
def main():
    gba_file = open('gettysburg.txt', 'r')

    newFile = input("What would you like the new file name to be?")
    processLine(gba_file)
    wordDic = addWord()
    prettyPrint(wordDic)


if __name__ == "__main__":
    main()
