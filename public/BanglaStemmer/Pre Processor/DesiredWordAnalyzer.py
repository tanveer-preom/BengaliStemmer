import re
import math
# from builtins import print

beforeWordList = {}
afterWordList = {}
ngram = 5
distanceFunction = "L"
beforeAndAfterWordFile = open('..\\Files\\Output Files\\BeforeAndAfterWord'+str(ngram)+'.txt', 'r', -1,'utf-8')
desiredWordSituation = open('..\\Files\\DesiredWordSituation'+str(distanceFunction)+str(ngram)+'.txt', 'w', -1,'utf-8')
desiredWordListFile = open('..\\Files\\Input Files\\DesiredWordList.txt', 'r', -1,'utf-8')

unigram = open('..\\Files\\Input Files\\Unigram.txt', 'r',-1,'utf-8')





# Distance Function D1
def spellingSimilarityD1(word1,word2):
    minlength = min(len(word1),len(word2))
    maxlength = max(len(word1),len(word2))
    # matchCount = 0

    for i in range(0,minlength):
        # print(word1[i]," ",word2[i])
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
    # print(maxlength)
    for i in range(0,minlength):
        if(word1[i] != word2[i]):
            break
    similarityp = 0
    for j in range(0, maxlength-i-1):
        similarityp = similarityp + (1/math.pow(2,j))
    return similarityp * (1/i)

# print(spellingSimilarityD2('মন', 'মনকে'))
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

def MN(word1,word2):
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
    return similarityMN
def MX(word1,word2):
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
    # similarityMN = (matchCountBefore + matchCountAfter)/(len(beforeWords1) + len(afterWords1))
    similarityMX = (matchCountBefore + matchCountAfter)/(len(beforeWords2) + len(afterWords2))
    return similarityMX

for line in beforeAndAfterWordFile:
    wordAndBeforeAfter = re.split(":", line)
    word = wordAndBeforeAfter[0].strip()
    beforeAndAfter = re.split("#", wordAndBeforeAfter[1])
    beforeWordList[word] = beforeAndAfter[0]
    afterWordList[word] = beforeAndAfter[1]

for line in desiredWordListFile:
    splits = line.split(":")
    root = splits[0].strip()

    words =  splits[1].split()


    for word in words:
        distance = str(levenshteinDistance(root, word.strip()))
        createString = root + " " + word + " D : " + distance +" MN : " +str(MN(root, word.strip()))+ " MX : " +str(MX(root, word.strip()))+ "\n"
        desiredWordSituation.write(createString)



print('Complete')
desiredWordSituation.close()
beforeAndAfterWordFile.close()
unigram.close()