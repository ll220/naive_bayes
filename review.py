# A class that is used in the process of parsing and categorizing data from the text files.
# It separates out each word into strings in an array, keeping a bag of words for each review and
# stores a separate value representing the class label 
# Also includes a function where an instance of the class can take a bag of vocabulary and add
# any additional words to the bag from its own words and sort the bag afterwards. 

class review:
    def __init__(self, words, classLabel):
        self.classLabel = classLabel    # Represents the class label 
        self.words = words  # Represents all the words found in the review

    def printReview(self):  # For debugging 
        print(self.words, self.classLabel)

    # Takes in a bag of vocabulary, tests its own words against the bag, and adds words not in the bag and then sorts it. 
    def addVocab(self, vocabList):  
        for i in self.words:
            if i in vocabList:
                pass 
            else:
                vocabList.append(i)

        vocabList.sort()