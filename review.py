

class review:
    def __init__(self, words, classLabel):
        self.classLabel = classLabel
        self.words = words

    def printReview(self):
        print(self.words, self.classLabel)

    def addVocab(self, vocabList): 
        for i in self.words:
            if i in vocabList:
                pass 
            else:
                vocabList.append(i)

        vocabList.sort()