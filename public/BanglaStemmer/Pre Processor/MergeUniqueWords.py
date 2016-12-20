import re
import operator
inputFile1 = open('..\\Files\\Input Files\\UniqueWords1.txt', 'r',-1,'utf-8')
inputFile2 = open('..\\Files\\Input Files\\UniqueWords2.txt', 'r',-1,'utf-8')
outputFile = open('..\\Files\\Input Files\\OutputUniqueWords.txt', 'w', -1,'utf-8')

dictionary = {}
i = 0;
for line in inputFile1:
    # print(line)
    word = line.strip()
    dictionary[word] = i
    i += 1
for line in inputFile2:
    # print(line)
    word = line.strip()
    dictionary[word] = i
    i += 1
sorted_word_list = sorted(dictionary.items(), key=operator.itemgetter(0))
# print(sorted_word_list)
# exit()
for word in sorted_word_list:
    # print(word[0])
    outputFile.write(word[0]+'\n')

# print(len(dictionary))



inputFile1.close()
inputFile1.close()
outputFile.close()

