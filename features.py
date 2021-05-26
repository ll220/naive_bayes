import review 

# A class that is used to store the vector of features and class label. The final product of the preprocessing and used in classification
# Takes in a review and the bag of vocabulary and stores a sequence of 0's and 1's in an array that corresponds to the vocabulary array, 
# where 1's represent the presence of that word in the review and 0 if not. The last element in the array is the value of the class label. 
class featureVector: 
    def __init__(self, review, vocabList):
        self.vector = []  
        for i in vocabList:     # Iterate through vocab and check if each word is in the review. 
            if i in review.words:
                self.vector.append(1)
            else:
                self.vector.append(0)

        self.vector.append(review.classLabel)   # Append the value of the class label as the last value in the 

    def printFeatureVector(self):
        print(self.vector)
