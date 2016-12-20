import re
import math
# from builtins import print

beforeWordList = {}
afterWordList = {}

ngram = 5
distance = "T"
beforeAndAfterWordFile = open('..\\Files\\Output Files\\BeforeAndAfterWord'+str(ngram)+'.txt', 'r', -1,'utf-8')
similarity = open('..\\Files\\Output Files\\Roots'+str(distance)+str(ngram)+'.txt', 'w', -1,'utf-8')
unigram = open('..\\Files\\Input Files\\Unigram.txt', 'r',-1,'utf-8')

unigram_words = {}
takenWord = {}
word_list = []
line_count = 0
root_list = {}
word_count = 0
minSpellingSimilarity = 0.1
minDistance = 4
minContextualSimilarity = 0.013
maxContextualSimilarity = 0.35

# print(2," *")
# exit()
def isTaken(word):
    if word in takenWord:
        return 1
    else:
        return 0
# Distance Function D1
def spellingSimilarityD1(word1,word2):
    minlength = min(len(word1),len(word2))
    maxlength = max(len(word1),len(word2))
    # matchCount = 0
    for i in range(0,minlength):
        if(word1[i] != word2[i]):
            break
    similarityp = 0
    for j in range(i+1, maxlength):
        similarityp = similarityp + (1/math.pow(2,j))
    return similarityp

# print(spellingSimilarityD1('মিলাইল', 'মিলাইলি'))
# exit()

# Distance Function D2

def spellingSimilarityD2(word1,word2):
    minlength = min(len(word1),len(word2))
    maxlength = max(len(word1),len(word2))
    # matchCount = 0
    for i in range(0,minlength):
        if(word1[i] != word2[i]):
            break
    similarityp = 0
    for j in range(i+1, maxlength):
        similarityp = similarityp + (1/math.pow(2,j))
    return similarityp * (1/4)

# Distance Function D2

def spellingSimilarityD2(word1,word2):
    minlength = min(len(word1),len(word2))
    maxlength = max(len(word1),len(word2))
    # print(maxlength)
    for i in range(0,minlength):
        if(word1[i] != word2[i]):
            break
    similarityp = 0
    for j in range(0, maxlength-i-1):
        similarityp = similarityp + (1/math.pow(2,j))
    return similarityp * (1/i)

# print(spellingSimilarityD2('astronomer', 'astronomically'))
# exit()

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def afterBeforeSimilarity(word1,word2):
    matchCountBefore = 0
    matchCountAfter = 0
    beforeWords1 = re.split(",", beforeWordList[word1])
    beforeWords2 = re.split(",", beforeWordList[word2])
    afterWords1 = re.split(",", afterWordList[word1])
    afterWords2 = re.split(",", afterWordList[word2])
    for word in beforeWords1:
        word = word.strip()
        if word in beforeWords2:
            matchCountBefore += 1
    for word in afterWords1:
        word = word.strip()
        if word in afterWords2:
            matchCountAfter += 1
    similarityMN = (matchCountBefore + matchCountAfter)/(len(beforeWords1) + len(afterWords1))
    similarityMX = (matchCountBefore + matchCountAfter)/(len(beforeWords2) + len(afterWords2))
    if similarityMN >= minContextualSimilarity and similarityMX >= maxContextualSimilarity:
        return 1
    else:
        return 0

for line in beforeAndAfterWordFile:
    # print("Line : ",line_count)
    wordAndBeforeAfter = re.split(":", line)
    line_count += 1
    word = wordAndBeforeAfter[0].strip()
    beforeAndAfter = re.split("#", wordAndBeforeAfter[1])
    # word_list.append(word)
    beforeWordList[word] = beforeAndAfter[0]
    afterWordList[word] = beforeAndAfter[1]
for word in unigram:
    word_list.append(word.strip())

for i, word in enumerate(word_list):
    print(i)
    j = i+1
    if isTaken(word) == 1:
        continue
    similarity.write("\n")
    similarity.write(str(word+" : "))
    root_list[word] = []
    takenWord[word] = 1

    while j < len(word_list):
        if isTaken(word_list[j]) == 1:
            j += 1
            continue
        temp = levenshteinDistance(word,word_list[j])
        if temp < minDistance:
            if spellingSimilarityD1(word, word_list[j]) < minSpellingSimilarity:
                if len(word) < len(word_list[j]):
                    continue
                if afterBeforeSimilarity(word, word_list[j]):
                    takenWord[word_list[j]] = 1
                    root_list[word].append(word_list[j])
                    similarity.write(str(word_list[j]+" "))
        else:
            if temp > minSpellingSimilarity + 0.2:
                break
        j += 1

print('Complete')
beforeAndAfterWordFile.close()
similarity.close()