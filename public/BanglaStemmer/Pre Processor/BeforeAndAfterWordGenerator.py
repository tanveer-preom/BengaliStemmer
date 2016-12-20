import re

beforeWordList = {}
afterWordList = {}

ngram = 2
unigram = open('..\\Files\\Input Files\\Unigram.txt', 'r',-1,'utf-8')
bigram = open('..\\Files\\Input Files\\Bigram.txt', 'r', -1,'utf-8')
output = open('..\\Files\\Output Files\\BeforeAndAfterWord'+str(ngram)+'.txt', 'w', -1,'utf-8')
unigram_words = {}
word_list = []
word_count = 0
line = 0

word_count = 0
for word in unigram:
    word = word.strip()
    beforeWordList[word] = {}
    afterWordList[word] = {}
    unigram_words[word] = word_count
    word_list.append(word)
    word_count += 1

for sentence in bigram:
    print(line)
    line += 1
    sentence = sentence.strip()
    words = sentence.split()
    for idx, word in enumerate(words):
        word = word.strip()
        try:
            for i in range(idx-1,idx-ngram-1,-1):
                if i < 0:
                    break
                beforeWordList[word][words[i].strip()] = 1
            for i in range(idx+1,idx+ngram+1):
                if i >= len(words):
                    break
                afterWordList[word][words[i].strip()] = 1
        except:
            continue
for word in word_list:
    output.write(word+" : ")
    out = ",".join(beforeWordList[word]) + " # "
    output.write(out)
    out = ",".join(afterWordList[word]) + "\n"
    output.write(out)





unigram.close()
bigram.close()
output.close()