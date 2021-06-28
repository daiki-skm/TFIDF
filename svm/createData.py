from random import seed
from random import sample


def createTrainTestData(tfidfdata, rate, vocSize, docSize, noTotaldata, classDoc, seedVal):
    tfidfWithClass = [[0.0 for x in range(vocSize+1)] for y in range(docSize)]

    noTrain = int(noTotaldata * (rate / 100))
    noTest = noTotaldata - noTrain

    for i in range(noTotaldata):
        tfidfWithClass[i] = tfidfdata[i]
        tfidfWithClass[i].insert(0, int(classDoc[i]))

    # print('tfidfWithClass = ', tfidfWithClass)
    # For Training Data
    seed(seedVal)
    train_idx_val = sample(list(enumerate(tfidfWithClass)), noTrain)
    total_indexes = [i for i in range(docSize)]
    train_indexes = []
    trainData = []
    for idx, val in train_idx_val:
        train_indexes.append(idx)
        trainData.append(val)
    # print('total_indexes = ', total_indexes)
    # print('train_indexes = ', train_indexes)

    # For Testing Data
    test_indexes = [item for item in total_indexes if item not in train_indexes]
    forTestDataSet = [tfidfWithClass[i] for i in test_indexes]
    testData = sample(forTestDataSet, noTest)

    # print('Train Data Set = ', trainData)
    # print('Test Data Set = ', testData)
    print('Number of Train Data = ', noTrain)
    print('Number of Test Data = ', noTest)

    return trainData, testData
