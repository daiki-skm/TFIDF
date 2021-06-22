import sys
import collections


def buildDictionaries(input_documents, docDataDic):
    # Build words and counter
    words = "".join(input_documents).split()
    count = collections.Counter(words).most_common()

    # Build dictionaries --> rdic, dic, docDataDic
    # rdic --- idx -> word
    # dic --- word -> id
    # docDataDic --- document -> id

    # Word Dictionaries --> rdic, dic
    rdic = [i[0] for i in count]  # reverse dic, idx -> word
    print('Size of Dictionary = ', len(rdic))
    dic = {w: i for i, w in enumerate(rdic)}  # dic, word -> id
    # Document Dictionary --> docDataDic
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
