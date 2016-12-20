import re
import operator

rootFile = "D25"
roots = open('..\\Files\\Output Files\\Roots'+rootFile+'.txt', 'r',-1,'utf-8')
sorted_list = open('..\\Files\\SortedRootByInflections'+rootFile+'.txt', 'w',-1,'utf-8')

lists = []
i = 0;
for line in roots:
    # print(line)
    tmp = line.split(":")
    root = tmp[0]
    inflections = tmp[1].split()
    dictionary = {}
    dictionary["root"] = root.strip()
    dictionary["count"] = len(inflections)
    lists.append(dictionary)

lists.sort(key=lambda x: x['count'],reverse=True)
for item in lists:
    outStr = item["root"]+ " "+ str(item["count"])+"\n"
    sorted_list.write(outStr)
# lists = sorted(dictionary.items(), key=operator.itemgetter(0))
# for line in lists:
#     print(line)





roots.close()
sorted_list.close()