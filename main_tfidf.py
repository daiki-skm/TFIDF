from caltfidf import cal_tfidf

with open("input.dat") as fp:
    input_documents = fp.readlines()
docTFIDFdata, rdic = cal_tfidf(input_documents)

print('Word Table = ', rdic)
print()

i = 0

for document in input_documents:
    print('Document: ', document.rstrip())
    print(docTFIDFdata[document])
    if i == 0:
        for test in docTFIDFdata[document].keys():
            print(docTFIDFdata[document][test])
    print()
    print()
    i += 1
