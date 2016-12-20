import re

bigram = open('..\\Files\\Input Files\\Bigram.txt', 'r',-1,'utf-8')
unigram = open('..\\Files\\Input Files\\UnigramNew.txt', 'w', -1,'utf-8')
word_list = {}
unsorted_words = []
i = 0
for line in bigram:
    i = i + 1
    print(i)
    words = line.split()
    for word in words:
        if word not in word_list:
            unsorted_words.append(word)
            word_list[word] = 1
for word in sorted(unsorted_words):
    unigram.write(word+"\n")

bigram.close()
unigram.close()