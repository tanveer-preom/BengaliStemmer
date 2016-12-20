import re
unigram = open('..\\Files\\Input Files\\Unigram.txt', 'w',-1,'utf-8')
bigram = open('..\\Files\\Input Files\\Bigram.txt', 'r', -1,'utf-8')

myre = re.compile(u'[\u0980-\u09FF]+', re.UNICODE)
i = 0
for line in input:

    # for c in line:
        # print(c)
        # print(repr(c))
    # print(line)

    m = re.sub('[^\u0980-\u09FF ]+','' , line.strip());
    if m:
        print(m)
        output.write(m+"\n")

input.close()
output.close()


