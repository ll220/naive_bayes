import preProcessing 
import setProbabilities
import review
import features
import re
import math 

trainingFeatureSets, trainVocabSize, testFeatureSets = preProcessing.allPreProcess()
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


trainTrainPredictions = getTrainingResults(trainingFeatureSets, trainVocabSize, trainingSetProbabilities)
trainTestPredictions = getTrainingResults(testFeatureSets, trainVocabSize, trainingSetProbabilities)

f = open("results.txt", "w")

f.write('Accuracy for trainingSet in training and testing: ')
f.write(str(trainTrainPredictions))
f.write("\n")
f.write('Accuracy for trainingSet in training and testSet in testing: ')
f.write(str(trainTestPredictions))
