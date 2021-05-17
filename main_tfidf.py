from caltfidf import cal_tfidf
from caltfidf import cos_sim
import numpy as np

# with open('input.dat') as fp:
with open('outcontents.txt') as fp:
    input_documents = fp.read().splitlines()
    # input_documents = fp.readlines()

print(input_documents)

# docTFIDFdata, rdic = cal_tfidf(input_documents)
#
# print('Word Table = ', rdic)
# print()
# print()
#
# for document in input_documents:
#     print('Document: ', document.rstrip())
#     print(docTFIDFdata[document])
#     print()
#     print()
#
# tfidfTable = [[0.0 for i in range(len(rdic))] for j in range(len(input_documents))]
#
# for i in range(len(input_documents)):
#     # print(docTFIDFdata[input_documents[i]])
#     # print(docTFIDFdata[input_documents[i]].keys())
#     for j in range(len(rdic)):
#         keysArr = docTFIDFdata[input_documents[i]].keys()
#         # print(keysArr)
#         for key in keysArr:
#             if rdic[j] == key:
#                 tfidfTable[i][j] = docTFIDFdata[input_documents[i]][key]
#
#
# resKey = []
# res = []
#
# for i in range(len(input_documents)):
#     for j in range(i + 1, len(input_documents)):
#         title = str(i+1) + ':' + str(j+1)
#         resKey.append(title)
#         x = np.array(tfidfTable[i])
#         y = np.array(tfidfTable[j])
#         res.append(cos_sim(x, y))
#
# propSort = sorted(dict(zip(resKey, res)).items(), key=lambda x: x[0])
# print(propSort)
#
# print()
# print()
#
# keySort = sorted(dict(zip(resKey, res)).items(), key=lambda x: x[1])
# print(keySort)
