import review
import features
import re

# Performs all of the preProcessing on text files. Includes reading them in, removing all punctuation and capitalization, 
# separating words and class labels, gathering words into a bag of vocabulary, forming feature vectors for each review, 
# writing information to a file, and returning the feature vectors. 

# Takes in file text and removes punctuation and capitalization
def removePuncLower(fileText):
    removedPunc = re.sub(r'[^\w\s]', '', fileText)
    noPuncLower = removedPunc.lower()
    return noPuncLower

# Reads in file, processes text and returns the text 
def parseFile(fileName):
    file = open(fileName, "r")
    fileText = file.read()
    processedText = removePuncLower(fileText)
    return processedText

# Splits each review apart from each other in file text, stored as a separate list item in an array 
def splitLines(processedText):
    lineArray = processedText.splitlines()
    return lineArray

# Takes each review and splits off the class label, then splits each word out from each other. 
# Makes an array such that [[[review 1 words], [review 1 label]], [[review 2 words], [review 2 label]], ...]
def splitClassLabel(lineArray):
    wordCLArray = []
    for i in lineArray:
        wordCLArray.append(i.split("\t"))

    for i in wordCLArray:
        i[0] = i[0].split()
        i[1] = i[1].split()

    return wordCLArray

# Transforms each review into a review class object, returns the array 
def makeReviewArray(wordCLArray):
    reviewArray = []
    for i in wordCLArray: 
        classLabel = 0
        if (i[1][0] == "1"):
            classLabel = 1

        newReview = review.review(i[0], classLabel)
        reviewArray.append(newReview)

    return reviewArray

# Creates a bag of vocabulary from array of reviews, should be done only for training set. It is automatically sorted with each review input
def getTrainingVocab(reviewArray):
    vocabList = []

    for i in reviewArray: 
        i.addVocab(vocabList)

    return vocabList

# Creates a featureVector class object for each review, returns an array of feature vectors
def makeFeatureSetArray(reviewArray, vocabList):
    featureSetArray = []

    for i in reviewArray: 
        newFeatureSet = features.featureVector(i, vocabList)
        featureSetArray.append(newFeatureSet)

    return featureSetArray

# Runs all preProcessing on both files, parsing text and creating featureVector arrays based on training vocabulary
def preProcessAllFiles():
    fileTextTrain = parseFile("trainingSet.txt")
    trainLineArray = splitLines(fileTextTrain)
    trainWordCLArray = splitClassLabel(trainLineArray)
    trainReviewArray = makeReviewArray(trainWordCLArray)
    trainVocab = getTrainingVocab(trainReviewArray)
    trainFeatureSetArray = makeFeatureSetArray(trainReviewArray, trainVocab)

    fileTextTest = parseFile("testSet.txt")
    testLineArray = splitLines(fileTextTest)
    testWordCLArray = splitClassLabel(testLineArray)
    testReviewArray = makeReviewArray(testWordCLArray)
    testFeatureSetArray = makeFeatureSetArray(testReviewArray, trainVocab)

    return trainFeatureSetArray, trainVocab, testFeatureSetArray

# Writes all information on the pre processing to an output file 
def writeToFile(featureSetArray, vocabList, outputFile):
    f = open(outputFile, "w")

    for i in vocabList:
        f.write(i)
        f.write(",")

    f.write("classlabel")
    f.write("\n")

    for i in featureSetArray:
        for j in i.vector:
            f.write(str(j))
            f.write(",")
        f.write("\n")

    f.close()

# Runs all pre processing on the training and testing sets, returns their vocab size and feature information and writes them to a file
def allPreProcess():

    trainingFeatureSets, trainingVocab, testFeatureSets = preProcessAllFiles()

    writeToFile(trainingFeatureSets, trainingVocab, "preprocessed_train.txt")
    writeToFile(testFeatureSets, trainingVocab, "preprocessed_test.txt")
    
    return trainingFeatureSets, len(trainingVocab), testFeatureSets
