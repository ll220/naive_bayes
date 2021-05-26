import preProcessing 
import setProbabilities
import review
import features
import re
import math 

# Driver data
# Carries out all classification and preprocessing, calculates conditional probability tables for the training data and testing phase for the training and 
# testing sets. 

# Carry out preprocessing and training phase on the training data
trainingFeatureSets, trainVocabSize, testFeatureSets = preProcessing.allPreProcess()
trainingSetProbabilities = setProbabilities.setProbs(trainingFeatureSets, trainVocabSize)

# Carries out classification of an inputted feature set
def getTrainingResults(featureSets, vocabSize, trainingSetProbabilities):
    numCorrectPredictions = 0   # Stores the number of accurate predictions made

    for i in featureSets:   # Iterate through every review 
        # Store the predicted probabilities for the class label
        probCLTrue = trainingSetProbabilities.cLTrueProb
        probCLFalse = trainingSetProbabilities.cLFalseProb


        for j in range(vocabSize):  # Iterate trough every vocab word

            # If the word exists in the review, then add its probability that it is true from training data given the predicted CL
            if (i.vector[j] == 1): 
                probCLTrue = probCLTrue + trainingSetProbabilities.featureProbArray[j].PTrueGivenTrue
                probCLFalse = probCLFalse + trainingSetProbabilities.featureProbArray[j].PTrueGivenFalse

            # Else, add its probability that it is false from training data given the predicted CL
            else:
                probCLTrue = probCLTrue + trainingSetProbabilities.featureProbArray[j].PFalseGivenTrue
                probCLFalse = probCLFalse + trainingSetProbabilities.featureProbArray[j].PFalseGivenFalse

        # Check the predicted class label. If predicted to be negative: 
        if (probCLFalse > probCLTrue):
            if (i.vector[vocabSize] == 0):  # Check if the actual class label is negative too
                numCorrectPredictions += 1
        else:
            if (i.vector[vocabSize] == 1):
                numCorrectPredictions += 1

    return (float(numCorrectPredictions) / float(len(featureSets))) # Return the percent of correctly guessed reviews


trainTrainPredictions = getTrainingResults(trainingFeatureSets, trainVocabSize, trainingSetProbabilities)
trainTestPredictions = getTrainingResults(testFeatureSets, trainVocabSize, trainingSetProbabilities)

# Print results to results.txt
f = open("results.txt", "w")

f.write('Accuracy for trainingSet in training and testing: ')
f.write(str(trainTrainPredictions))
f.write("\n")
f.write('Accuracy for trainingSet in training and testSet in testing: ')
f.write(str(trainTestPredictions))
