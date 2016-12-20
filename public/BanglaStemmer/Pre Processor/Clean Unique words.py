import re


def cleanWordlist(file):

    words = open(file,'r', -1,'utf-8')
    write = open(file,'w', -1,'utf-8')
    for line in words:
        word = line.strip()
        word = re.sub('[^\u0980-\u09FF]+', '', word)
        write.write(m + "\n")

    words.close(file,)
    write.close()
input = '..\\Files\\Input Files\\UniqueWords1.txt'
cleanWordlist(input)
input = '..\\Files\\Input Files\\UniqueWords2.txt'
cleanWordlist(input)

