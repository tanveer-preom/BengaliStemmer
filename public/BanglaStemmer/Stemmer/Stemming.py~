import re
import math
import sys
# from builtins import print

rootWords = []
afterWordList = {}

inputFile = sys.argv[1]
outputFile = sys.argv[2]
ld5file = sys.argv[3]
testdata = open(inputFile, 'r', -1,'utf-8')
roots = open(ld5file, 'r', -1,'utf-8')
output = open(outputFile, 'w', -1,'utf-8')

for root in roots:
    # print("Line : ",line_count)

    temp  = root.split(":")
    # print(temp)
    rootWords.append({'root' : temp[0].strip(), 'inflections' : temp[1].split()})

# greats = ["অংকই", "অংক", "অংকটাকে"]
# for great in greats:
#     if great is "অংক":
#         print(great)
# if "অংক" is "অংক":
#     print("ok")

def findRoot(word):
    i = 0
    for rootWord in rootWords:


        # print(rootWord['root'])


        # print(rootWord['inflections'])
        inflections = rootWord['inflections']
        # print(rootWord['root'])
        for inflection in inflections:
        #      print()
             if inflection.strip() == word:
                 return rootWord['root']
    return word

# for rootWord in rootWords:
#     print(rootWord)
i = 0
for line in testdata:
    words = line.split()
    for word in words:
        word = re.sub("[,‘।]", "", word.strip())
        rootForm = findRoot(word)
        generateOutput = word+" : "+rootForm+"\n"
        output.write(generateOutput)
print(findRoot("অংকই"))
output.close()


testdata.close()
roots.close()
