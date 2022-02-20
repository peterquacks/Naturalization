#! python3
import sys
import re
import random

def load(ver):
    filename = ver + ".txt"    
    file = open(filename, "r")

    ### This will be the regex pattern where it finds a number and a period afterwards which is consistent in txt files.
    questionLine = "[\d]+\."
    
    # create a dictionary with question key and answer tuple
    pDict = {}
    
    answer = []

    # search for lines containing qusetions. Set as Key pair.
    # Will populate question key if answer is not empty.
    # else if check to see if it's not empty line

    for line in file.readlines():
        if re.search(questionLine, line):
            if answer:
                pDict[question] = answer
                answer = []
            question = line.strip()
        
        elif not re.search("^s*$", line):
            answer = answer + [line.strip()]
    
    # For last entry since there's no new question
    pDict[question] = answer
    file.close()

    pick_random(pDict)


def pick_random(qDict):

    # Randomize the keys in the dictionary
    keys = list(qDict.keys())
    random.shuffle(keys)

    
    wrongAnswer = []

    
    for i in range(0,len(qDict) - 1):
        response = input(keys[i] + "\n")
        value    = qDict[keys[i]]
        val      = []

        # Loop through list and sets each string of list to lowercase to avoid case sensitive checking
        for j in value:
            word = j.lower()
            val = val + [word]

        
        if response.lower() in val:
            print ("Nice job! You are correct! Here are the following possible answers. \n")
            print (qDict[keys[i]])
        
        else:
            print ("Sorry, you did not get the answer correct. The following answer(s) are: \n")
            print (qDict[keys[i]])
            wrongAnswer.append(keys[i])
    
    # Try again until you get it right
    if wrongAnswer:
        for i in range(0,len(wrongAnswer)):
            response = input(wrongAnswer[i])






def main():

    usage = "Please enter which naturalization test you are going to be tested on. Type \"2008\" or \"2020\" and Enter.\n"
    version = str(input(usage))

    
    if version == "2020" or version == "2008":
        load(version)

    else:
        print ("Incorrect value. Please try again and choose either 2008 or 2020 and press enter.")



if __name__ == "__main__":
    main()