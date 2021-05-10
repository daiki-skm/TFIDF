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

# allArr = [][]

# allArr = np.array([[0] * minNum for i in range(10)])

i = 0
j = 0

for document in input_documents:
    print('Document: ', document.rstrip())
    print(docTFIDFdata[document])
    for kw in docTFIDFdata[document].keys():
        print(docTFIDFdata[document][kw])
        if j < minNum:
            allArr[i][j] = docTFIDFdata[document][kw]
        j += 1
    print()
    print()
    i += 1
    j = 0

# X = np.array([0.789, 0.515, 0.335, 0])
# Y = np.array([0.832, 0.555, 0, 0])
#
# print(cos_sim(X, Y))

print(allArr)
