from scraping import get_article
from getFromFiles import getProcessedContentsByLineFromFiles
from build import buildDictionaries
from caltfidf import cal_tfidf
from getidxtfidf import getidxTFIDF
from createData import createTrainTestData
from analysis import analysis


noPdata = 0            # number of business data (documents)
noNdata = 0            # number of technology data (documents)
noTotaldata = 0        # number of Total data (documents)
vocSize = 0            # size of vocabulary
docSize = 0            # size of documents
rdic = []              # idx -> word
dic = {}               # word -> id
docDataDic = {}        # document -> id
input_documents = []   # contents of whole input documents
classDoc = []          # class information of all documents
docTFIDFdata = {}      # TFIDF data of all documents

inFileNames = ['pData.txt', 'nData.txt']  # Input File Names for business and technology
trainRate = 60         # Portion of Training Data (Rate/100)
seedVal = 1            # seed value for random sampling
dataColWidth = 100     # Width (number of column - features) for training and test data


get_article()

input_documents, lineContentsp, lineContentsn = getProcessedContentsByLineFromFiles(inFileNames[0], inFileNames[1])

noPdata = len(lineContentsp)
noNdata = len(lineContentsn)
noTotaldata = len(input_documents)

print('Size of Positive line document data = ', noPdata)
print('Size of Negative line document data = ', noNdata)
print('Size of Total line document data = ', noTotaldata)

rdic, dic, docDataDic = buildDictionaries(input_documents, docDataDic)

docTFIDFdata = cal_tfidf(docDataDic)

tfidfval, docSize, vocSize, classDoc = getidxTFIDF(docDataDic, dic, noTotaldata, docTFIDFdata, noPdata)

trainData, testData = createTrainTestData(tfidfval, trainRate, vocSize, docSize, noTotaldata, classDoc, seedVal)

analysis(trainData, testData, dataColWidth)
