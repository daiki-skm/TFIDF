from getFromFiles import getProcessedContentsByLineFromFiles
from build import buildDictionaries
from caltfidf import cal_tfidf
from getidxtfidf import getidxTFIDF
from createData import createTrainTestData
from analysis import analysis

inFileNames = ['pData.txt', 'nData.txt']  # Input File Names for business and technology
docDataDic = {}        # document -> id
trainRate = 60         # Portion of Training Data (Rate/100)
seedVal = 1            # seed value for random sampling
dataColWidth = 100     # Width (number of column - features) for training and test data

input_documents, lineContentsp, lineContentsn = getProcessedContentsByLineFromFiles(inFileNames[0], inFileNames[1])

noPdata = len(lineContentsp)
noNdata = len(lineContentsn)
noTotaldata = len(input_documents)

print('Size of Positive line document data = ', noPdata)
print('Size of Negative line document data = ', noNdata)
print('Size of Total line document data = ', noTotaldata)

rdic, dic, docDataDic = buildDictionaries(input_documents, docDataDic)

docTFIDFdata = cal_tfidf(docDataDic)

tfidfval, docSize, vocSize, classDoc = getidxTFIDF(docDataDic, dic, docTFIDFdata, noTotaldata, noPdata)

trainData, testData = createTrainTestData(tfidfval, trainRate, vocSize, docSize, noTotaldata, classDoc, seedVal)

analysis(trainData, testData, dataColWidth)
