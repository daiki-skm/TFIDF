from caltfidf import cal_tfidf
from caltfidf import cos_sim
import numpy as np

with open('input.dat') as fp:
    input_documents = fp.readlines()
docTFIDFdata, rdic = cal_tfidf(input_documents)

print('Word Table = ', rdic)
print()
print()

lenArr = []
for document in input_documents:
    lenArr.append(len(docTFIDFdata[document]))
minArrNum = min(lenArr)
allNumArr = [[0.0] * minArrNum for i in range(10)]

i = 0
j = 0

for document in input_documents:
    print('Document: ', document.rstrip())
    print(docTFIDFdata[document])
    for kw in docTFIDFdata[document].keys():
        if j < minArrNum:
            allNumArr[i][j] = docTFIDFdata[document][kw]
        j += 1
    print()
    print()
    i += 1
    j = 0

res = []
resKey = []

for i in range(len(allNumArr)):
    for j in range(i+1, 10):
        title = 'S' + str(i) + ':' + 'E' + str(j)
        resKey.append(title)
        x = np.array(allNumArr[i])
        y = np.array(allNumArr[j])
        res.append(cos_sim(x, y))

# print(res)
# print(resKey)

print(dict(zip(resKey, res)))
