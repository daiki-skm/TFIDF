import nltk


def getNltkWordList():
    # f = open('input.dat')
    f = open('outcontents.txt')
    raw = f.read()
    # raw = f.read().splitlines()
    print('raw data..')
    print(raw)
    # for demo in raw:
    #     print(demo)
    token = nltk.word_tokenize(raw)
    token_tag = nltk.pos_tag(token)
    # print('Contents with tag...', token_tag)
    print()

    list = []

    for word, tag in token_tag:
        # print(word, tag)
        # JJ:形容詞, NN:名詞, VB:動詞
        if tag.startswith('JJ') or tag.startswith('NN') or tag.startswith('VB'):
            list.append(word)

    print(list)

    return list


tmp = getNltkWordList()
# print(tmp)
