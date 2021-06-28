def getidxTFIDF(docDataDic, dic, docTFIDFdata, noTotaldata, noPdata):
    docSize = len(docDataDic.keys())
    vocSize = len(dic)
    tfIDFval = [[0.0 for x in range(vocSize)] for y in range(docSize)]
    classDoc = [0 for i in range(noTotaldata)]

    docindex = 0
    for document in docDataDic.keys():
        thisDoc = docDataDic.get(document)
        # dataListWordVal = [(x, docTFIDFdata[thisDoc].get(x)) for x in docTFIDFdata[thisDoc].keys()]
        # dataListWordVal = docTFIDFdata[thisDoc].most_common()
        for x in docTFIDFdata[thisDoc].keys():
            if dic.get(x) is None:
                continue
            tfIDFval[docindex][dic.get(x)] = docTFIDFdata[thisDoc].get(x)
        if (docindex < noPdata):
            classDoc[docindex] = 1
        else:
            classDoc[docindex] = -1
        docindex = docindex + 1
    return tfIDFval, docSize, vocSize, classDoc
