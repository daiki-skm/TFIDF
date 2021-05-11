import math
import collections
from collections import Counter
from collections import defaultdict
import numpy as np


def cal_tfidf(input_documents):
    N = len(input_documents)
    words = ''.join(input_documents).split()
    count = collections.Counter(words).most_common()

    # Build dictionaries
    rdic = [i[0] for i in count]  # reverse dic, idx -> word

    # Calculating TFIDF
    docTFtable = defaultdict(Counter)
    DFtable = Counter()
    docTFIDFtable = defaultdict(Counter)

    for document in input_documents:
        words = document.split()
        for word in words:
            docTFtable[document][word] += 1

        for kw in docTFtable[document].keys():
            DFtable[kw] += 1

    for document in input_documents:
        for kw in docTFtable[document].keys():
            docTFIDFtable[document][kw] = docTFtable[document][kw] * math.log(N / DFtable[kw])

    return docTFIDFtable, rdic


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
