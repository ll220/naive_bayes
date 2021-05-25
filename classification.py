import preProcessing 
import setProbabilities
import review
import features
import re
import math 

trainingFeatureSets, trainVocabSize, testFeatureSets, testVocabSize = preProcessing.allPreProcess()
trainingSetProbabilities = setProbabilities.setProbs(trainingFeatureSets, trainVocabSize)


def getTrainingResults(featureSets, vocabSize, trainingSetProbabilities):
    numCorrectPredictions = 0

    for i in featureSets:
        probCLTrue = trainingSetProbabilities.cLTrueProb
        probCLFalse = trainingSetProbabilities.cLFalseProb


        for j in range(vocabSize):
            if (i.vector[j] == 1): 
                probCLTrue = probCLTrue + trainingSetProbabilities.featureProbArray[j].PTrueGivenTrue
                probCLFalse = probCLFalse + trainingSetProbabilities.featureProbArray[j].PTrueGivenFalse

            else:
                probCLTrue = probCLTrue + trainingSetProbabilities.featureProbArray[j].PFalseGivenTrue
                probCLFalse = probCLFalse + trainingSetProbabilities.featureProbArray[j].PFalseGivenFalse

        if (probCLFalse > probCLTrue):
            if (i.vector[vocabSize] == 0): 
                numCorrectPredictions += 1
        else:
            if (i.vector[vocabSize] == 1): 
                numCorrectPredictions += 1

    return (float(numCorrectPredictions) / float(len(featureSets)))


print('Accuracy for trainingSet in training and testing: ', getTrainingResults(trainingFeatureSets, trainVocabSize, trainingSetProbabilities))
print('Accuracy for trainingSet in training and testSet in testing: ', getTrainingResults(testFeatureSets, trainVocabSize, trainingSetProbabilities))
