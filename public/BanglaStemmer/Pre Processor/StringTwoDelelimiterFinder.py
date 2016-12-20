import re
input = open('Sorted Unique Words.txt', 'r',-1,'utf-8')
output = open('Sorted Unique Words_n.txt', 'w', -1,'utf-8')

# myre = re.compile(u'[\u0980-\u09FF]+', re.UNICODE)
limit = 0
i = 0


wordMappingByInteger = []
words_list = {}
for line in input:
    word = line.strip()
    words_list[word] = i
    wordMappingByInteger.insert(i, word)
    i += 1
    # print(line)
length = len(words_list)
i = words_list['অক্ষ']
for i in range(i,length):
    # print(i)
    k = 0
    for j in range(i+1, length):
        # print(wordMappingByInteger[i]," ", wordMappingByInteger[j])


        pattern = "^"+wordMappingByInteger[i]+"(.*)"
        # print(pattern)
        # exit()
        isMatch = re.search(pattern, wordMappingByInteger[j])
        # print(isMatch)
        # exit()
        if isMatch:
            # print(isMatch.string)
            # print(k)
            k += 1
        else:
            break

    limit = k

    if limit > 2000:
        print('Paisi')
        print('For ', wordMappingByInteger[i] , 'Limit' , limit)

        # exit()


input.close()
output.close()


