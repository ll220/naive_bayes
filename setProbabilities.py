import math

# A class that stores the conditional probability tables for the training set class label and the features based on the feature vector. 
# The feature probability table is stored in the featureProb class and the setProbs stores an array of featureProbs to represent 
# The probability table of each word in the vocabulary. 
# This class should only be performed on the training set. 

# Stores a single conditional probability table for a feature, or a vocabulary word 
class featureProb():
    def __init__(self, featureSets, vocabSize, cLTrueNum, cLFalseNum, featureIndex):
        # Stores the number of occurences for feature = t/f and classLabel = t/f
        falseAndFalse, falseAndTrue, trueAndFalse, trueAndTrue = 0, 0, 0, 0

        # Iterate through each review and check the occurence of the specific feature and the class label
        for i in featureSets:
            if (i.vector[featureIndex] == 0 and i.vector[vocabSize] == 0):
                falseAndFalse += 1
            elif (i.vector[featureIndex] == 0 and i.vector[vocabSize] == 1):
                falseAndTrue += 1
            elif (i.vector[featureIndex] == 1 and i.vector[vocabSize] == 0):
                trueAndFalse += 1 
            else: 
                trueAndTrue += 1

        # Calculate probabilities using log base 10 and dirichlet priors
        self.PTrueGivenTrue = math.log10(float(trueAndTrue + 1) / float(cLTrueNum + 2))
        self.PFalseGivenTrue = math.log10(float(falseAndTrue + 1) / float(cLTrueNum + 2))
        self.PTrueGivenFalse = math.log10(float(trueAndFalse + 1) /float(cLFalseNum + 2))
        self.PFalseGivenFalse = math.log10(float(falseAndFalse + 1) /float(cLFalseNum + 2))


# Stores the probability table for the class labels and an array of conditional probability tables for each element in the vocabulary
class setProbs(featureProb): 
    def __init__(self, featureSets, vocabSize):
        cLTrueNum = 0   # Store number of occurences where the class label is 1

        # Iterate through each review and check its class label
        for i in featureSets: 
            if (i.vector[vocabSize]):
                cLTrueNum += 1

        cLFalseNum = len(featureSets) - cLTrueNum
        self.featureProbArray = []  # Store the feature probability tables

        # Iterate through all vocabulary and create conditional probability tables for each 
        for n in range(vocabSize):
            newFeatureProb = featureProb(featureSets, vocabSize, cLTrueNum, cLFalseNum, n)
            self.featureProbArray.append(newFeatureProb)

        # Using log space, calculate probabilities for class label 
        self.cLFalseProb = math.log10(float(cLFalseNum) / float(len(featureSets)))
        self.cLTrueProb = math.log10(float(cLTrueNum) / float(len(featureSets)))




