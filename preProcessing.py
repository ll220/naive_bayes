import review
import features
import re

def removePuncLower(fileText):
    removedPunc = re.sub(r'[^\w\s]', '', fileText)
    noPuncLower = removedPunc.lower()
    return noPuncLower

def parseFile(fileName):
    file = open(fileName, "r")
    fileText = file.read()
    processedText = removePuncLower(fileText)
    return processedText

def splitLines(processedText):
    lineArray = processedText.splitlines()
    return lineArray

def splitClassLabel(lineArray):
    wordCLArray = []
    for i in lineArray:
        wordCLArray.append(i.split("\t"))

    for i in wordCLArray:
        i[0] = i[0].split()
        i[1] = i[1].split()

    return wordCLArray

def makeReviewArray(wordCLArray):
    reviewArray = []
    for i in wordCLArray: 
        classLabel = 0
        if (i[1][0] == "1"):
            classLabel = 1

        newReview = review.review(i[0], classLabel)
        reviewArray.append(newReview)

    return reviewArray

def getVocab(reviewArray):
    vocabList = []

    for i in reviewArray: 
        i.addVocab(vocabList)

    return vocabList

def makeFeatureSetArray(reviewArray, vocabList):
    featureSetArray = []

    for i in reviewArray: 
        newFeatureSet = features.featureVector(i, vocabList)
        featureSetArray.append(newFeatureSet)

    return featureSetArray

def preProcessOneFile(fileName):
    fileText = parseFile(fileName)
    lineArray = splitLines(fileText)
    wordCLArray = splitClassLabel(lineArray)
    reviewArray = makeReviewArray(wordCLArray)
    vocabList = getVocab(reviewArray)
    featureSetArray = makeFeatureSetArray(reviewArray, vocabList)

    return featureSetArray, vocabList

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

def allPreProcess():
    trainingFeatureSets, trainingVocab = preProcessOneFile("trainingSet.txt")
    testFeatureSets, testVocab = preProcessOneFile("testSet.txt")
    writeToFile(trainingFeatureSets, trainingVocab, "preprocessed_train.txt")
    writeToFile(testFeatureSets, testVocab, "preprocessed_test.txt")
    
    return trainingFeatureSets, len(trainingVocab), testFeatureSets, len(testVocab)
