import sys
import collections


def buildDictionaries(input_documents, docDataDic):
    words = "".join(input_documents).split()
    count = collections.Counter(words).most_common()

    # rdic --- idx -> word
    # dic --- word -> id
    # docDataDic --- document -> id

    rdic = [i[0] for i in count]
    print('Size of Dictionary = ', len(rdic))
    dic = {w: i for i, w in enumerate(rdic)}
    for i, doc in enumerate(input_documents):
        v = docDataDic.get(doc)
        if v is None:
            docDataDic[doc] = i
        else:
            print('Fatal Error in Data! You have the same contents in your documents. Remove the data record below and try again. Terminating.. ')
            print('The record index = ', i)
            print('The content of the record = \n', doc)
            sys.exit()

    return rdic, dic, docDataDic
