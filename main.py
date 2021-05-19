from caltfidf import cal_tfidf
from caltfidf import cos_sim
import numpy as np
from testnltk import get_nltk_word_list
from requesthtml import get_article


get_article()

with open('outcontents.txt') as fp:
    input_documents = fp.read().splitlines()

documents_list = []

for word in input_documents:
    if word != '':
        documents_list.append(word)

# print(input_documents)
# print()
# print()
#
# print(documents_list)
# print()
# print()

docTFIDFdata, _ = cal_tfidf(documents_list)

# print(docTFIDFdata)
# print()
# print()

nltkData = get_nltk_word_list()

print('NLTK Word Table= ', nltkData)
print()
print()

tfidfTable = [[0.0 for i in range(len(nltkData))] for j in range(len(documents_list))]

# print(tfidfTable)

for i in range(len(documents_list)):
    # print(docTFIDFdata[input_documents[i]])
    # print(docTFIDFdata[input_documents[i]].keys())
    for j in range(len(nltkData)):
        keysArr = docTFIDFdata[documents_list[i]].keys()
        # print(keysArr)
        for key in keysArr:
            if nltkData[j] == key:
                tfidfTable[i][j] = docTFIDFdata[documents_list[i]][key]
            else:
                continue

resKey = []
res = []

for i in range(len(documents_list)):
    for j in range(i + 1, len(documents_list)):
        title = str(i+1) + ':' + str(j+1)
        x = np.array(tfidfTable[i])
        y = np.array(tfidfTable[j])
        cossim = cos_sim(x, y)
        if cossim != 0:
            resKey.append(title)
            res.append(cossim)
        else:
            continue

# print(resKey)
# print(res)

propSort = sorted(dict(zip(resKey, res)).items(), key=lambda x: x[0])
print(propSort)

print()
print()

keySort = sorted(dict(zip(resKey, res)).items(), key=lambda x: x[1])
print(keySort)
