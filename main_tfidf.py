from caltfidf import cal_tfidf
from caltfidf import cos_sim
import numpy as np

with open("input.dat") as fp:
    input_documents = fp.readlines()
docTFIDFdata, rdic = cal_tfidf(input_documents)

print('Word Table = ', rdic)
print()

lenArr = []

for document in input_documents:
    lenArr.append(len(docTFIDFdata[document]))

minNum = min(lenArr)

allArr = [[0.0] * minNum for i in range(10)]

i = 0
j = 0

for document in input_documents:
    print('Document: ', document.rstrip())
    print(docTFIDFdata[document])
    for kw in docTFIDFdata[document].keys():
        if j < minNum:
            allArr[i][j] = docTFIDFdata[document][kw]
        j += 1
    print()
    print()
    i += 1
    j = 0

res = []

for i in range(len(allArr)):
    for j in range(i+1, 10):
        x = np.array(allArr[i])
        y = np.array(allArr[j])
        res.append(cos_sim(x, y))

print(res)
