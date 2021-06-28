import math
from collections import Counter
from collections import defaultdict


def cal_tfidf(docDataDic):
    N = len(docDataDic.keys())

    docTFtable = defaultdict(Counter)
    DFtable = Counter()
    docTFIDFtable = defaultdict(Counter)

    for document in docDataDic.keys():
        words = document.split()
        thisDoc = docDataDic.get(document)

        for word in words:
            docTFtable[thisDoc][word] += 1

        for kw in docTFtable[thisDoc].keys():
            DFtable[kw] += 1

    for document in docDataDic.keys():
        thisDoc = docDataDic.get(document)
        for kw in docTFtable[thisDoc].keys():
            docTFIDFtable[thisDoc][kw] = docTFtable[thisDoc][kw] * math.log(N / DFtable[kw])

    return docTFIDFtable
