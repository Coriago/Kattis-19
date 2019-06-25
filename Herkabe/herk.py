import sys
import math
import functools
#Author: Gage Miller
#Date: 6/20/19
#All combinations in which beginning sequences are next to each other and similar ones are in between.


# Takes a list and finds the largest prefix with a match and returns the amount 
# of matches while removing all words with the prefix
def largestPrefix(strs):
    # Return 0 if list is empty
    if not strs:
        return 0
    
    # Sorts the list by length largest top
    strs.sort(key=len, reverse=True)

    # Initial size assumed to be the largest word, and match variables set
    prefixSize = len(strs[0])
    matchFound = False
    matches = 1

    while(not matchFound and prefixSize > 0):
        for word in strs:
            # Try to get a prefix out of the word. If word is to small move to smaller prefix
            if(len(word) >= prefixSize):
                prefix = word[:prefixSize]
                for i, matchWord in enumerate(strs):
                    # Try to find a match for the prefix
                    if(matchWord != word and matchWord.startswith(prefix)):
                        matchFound = True
                        matches += 1
                        strs.remove(matchWord)
                if matchFound: 
                    strs.remove(word)
                    break        
            else:
                break

        # Search for a smaller prefix
        prefixSize -= 1
        # If no prefix could be found, only unique words are left
        # Pop a unique word and return a match of 1
        if prefixSize == 0 and not matchFound:
            strs.pop()
    return matches



# Main function
def run():

    #Gather all words
    words = []
    first = True
    for line in sys.stdin:
        if(first):
            first = False
        else:
            words.append(line.strip())

    #find all matches of prefixes and add to combos
    combos = []
    while(words):
        combos.append(largestPrefix(words))

    #Compute total combinations
    total = 1
    for c in combos:
        total *= math.factorial(c)

    print(total * math.factorial(len(combos)))
    
    


if __name__ == "__main__":
    run()