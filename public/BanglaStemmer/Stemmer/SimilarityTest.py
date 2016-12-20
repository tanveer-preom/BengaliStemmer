import re

# from builtins import print

beforeWordList = {}
afterWordList = {}


beforeAndAfterWordFile = open('..\\Files\\Output Files\\BeforeAndAfterWord.txt', 'r', -1,'utf-8')
similarity = open('..\\Files\\Output Files\\SimilarityTest.txt', 'w', -1,'utf-8')
unigram = open('..\\Files\\Input Files\\UnigramTest.txt', 'r',-1,'utf-8')
unigram_words = {}
takenWord = {}
word_list = []
line_count = 0
root_list = {}
word_count = 0
minSpellingSimilarity = 70
minContextualSimilarity = 0.018
maxContextualSimilarity = 0.335


def isTaken(word):
    if word in takenWord:
        return 1
    else:
        return 0
def spellingSimilarity(word1,word2):
    minlength = min(len(word1),len(word2))
    matchCount = 0
    for i in range(0,minlength):
        if(word1[i] == word2[i]):
            matchCount += 1
        else:
            break
    similarityp =  (matchCount/minlength)*100
    # similarity.write("("+word1+","+word2+")")
    # similarity.write(str(similarityp)+"\n")
    return similarityp

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
    print(similarityMN , " ", similarityMX)
    if similarityMN >= minContextualSimilarity and similarityMX >= maxContextualSimilarity:
        return 1
    else:
        return 0

for line in beforeAndAfterWordFile:
    print("Line : ",line_count)
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
    similarity.write(str(word+" : "))
    if isTaken(word) == 1:
        similarity.write("\n")
        continue
    root_list[word] = []
    takenWord[word] = 1
    j = i+1
    while j < len(word_list):
        if isTaken(word_list[j]) == 1:
            j += 1
            continue
        if spellingSimilarity(word,word_list[j]) >= minSpellingSimilarity:
            # similarity.write("\n")
            if afterBeforeSimilarity(word, word_list[j]) == 1:
                takenWord[word_list[j]] = 1
                root_list[word].append(word_list[j])
                similarity.write(str(word_list[j]+","))
        j += 1
    similarity.write("\n")


print(afterBeforeSimilarity('অক্ষ', 'অক্ষই'))





print("Complete")

beforeAndAfterWordFile.close()
similarity.close()