import nltk


def get_nltk_word_list():
    f = open('outcontents.txt')
    raw = f.read()
    # print('raw data..')
    # print(raw)

    token = nltk.word_tokenize(raw)
    token_tag = nltk.pos_tag(token)
    # print('Contents with tag...', token_tag)
    # print()

    wordList = []

    for word, tag in token_tag:
        # print(word, tag)
        # JJ:形容詞, NN:名詞, VB:動詞
        if tag.startswith('JJ') or tag.startswith('NN') or tag.startswith('VB'):
            wordList.append(word)
        else:
            continue

    # print(list)

    return wordList
