import preProcessing 
import setProbabilities
import review
import features
import re
import math 

trainingFeatureSets, trainVocabSize, trainVocab, testFeatureSets, testVocabSize, testVocab = preProcessing.allPreProcess()


def getTrainingResults(trainingFeatureSets, trainVocabSize):
    trainingSetProbabilities = setProbabilities.setProbs(trainingFeatureSets, trainVocabSize)
    numCorrectPredictions = 0

    for i in trainingFeatureSets:
        probCLTrue = trainingSetProbabilities.cLTrueProb
        probCLFalse = trainingSetProbabilities.cLFalseProb


        for j in range(trainVocabSize):
            if (i.vector[j] == 1): 
                probCLTrue = probCLTrue + trainingSetProbabilities.featureProbArray[j].PTrueGivenTrue
                probCLFalse = probCLFalse + trainingSetProbabilities.featureProbArray[j].PTrueGivenFalse

            else:
                probCLTrue = probCLTrue + trainingSetProbabilities.featureProbArray[j].PFalseGivenTrue
                probCLFalse = probCLFalse + trainingSetProbabilities.featureProbArray[j].PFalseGivenFalse

        if (probCLFalse > probCLTrue):
            if (i.vector[trainVocabSize] == 0): 
                numCorrectPredictions += 1
        else:
            if (i.vector[trainVocabSize] == 1): 
                numCorrectPredictions += 1
                
    return (float(numCorrectPredictions) / float(len(trainingFeatureSets)))


print(getTrainingResults(trainingFeatureSets, trainVocabSize))
