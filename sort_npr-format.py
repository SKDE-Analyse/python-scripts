

import sys

filename = sys.argv[1]
infile = open(filename, "r")

num = 0
sort_list = []
neste = False
first = True
block = ""
for i in infile.readlines():
    if i[0] == '*' or not i.strip():
        continue
    if 'value' in i:
        if not first:
            sort_list.append([label,block])
        label = i.split()[1]
        if first:
            first = False
        block = i
        num += 1
        neste = True
    else:
        i = i.replace('"', "'")
        block += i

sort_list.append([label,block])

test = sorted(sort_list)

for k in range(num):
    print(test[k][1])
    print("")
    print("")
    print("")



