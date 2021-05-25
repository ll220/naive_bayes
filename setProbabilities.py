import math

class featureProb():
    def __init__(self, featureSets, vocabSize, cLTrueNum, cLFalseNum, featureIndex):
        falseAndFalse, falseAndTrue, trueAndFalse, trueAndTrue = 0, 0, 0, 0

        for i in featureSets:
            if (i.vector[featureIndex] == 0 and i.vector[vocabSize] == 0):
                falseAndFalse += 1
            elif (i.vector[featureIndex] == 0 and i.vector[vocabSize] == 1):
                falseAndTrue += 1
            elif (i.vector[featureIndex] == 1 and i.vector[vocabSize] == 0):
                trueAndFalse += 1 
            else: 
                trueAndTrue += 1

        self.PTrueGivenTrue = math.log10(float(trueAndTrue + 1) / float(cLTrueNum + 2))
        self.PFalseGivenTrue = math.log10(float(falseAndTrue + 1) / float(cLTrueNum + 2))
        self.PTrueGivenFalse = math.log10(float(trueAndFalse + 1) /float(cLFalseNum + 2))
        self.PFalseGivenFalse = math.log10(float(falseAndFalse + 1) /float(cLFalseNum + 2))



class setProbs(featureProb): 
    def __init__(self, featureSets, vocabSize):
        cLTrueNum = 0

        for i in featureSets: 
            if (i.vector[vocabSize]):
                cLTrueNum += 1

        cLFalseNum = len(featureSets) - cLTrueNum
        self.featureProbArray = []

        for n in range(vocabSize):
            newFeatureProb = featureProb(featureSets, vocabSize, cLTrueNum, cLFalseNum, n)
            self.featureProbArray.append(newFeatureProb)

        self.cLFalseProb = math.log10(float(cLFalseNum) / float(len(featureSets)))
        self.cLTrueProb = math.log10(float(cLTrueNum) / float(len(featureSets)))




