import review 

class featureVector: 
    def __init__(self, review, vocabList):
        self.vector = []
        for i in vocabList:
            if i in review.words:
                self.vector.append(1)
            else:
                self.vector.append(0)

        self.vector.append(review.classLabel)

    def printFeatureVector(self):
        print(self.vector)
