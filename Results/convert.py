import sys
from os import walk
import os
import csv
a = sys.argv[1]


f = []
for (dirpath, dirnames, filenames) in walk(a):
    f.extend(filenames)
    break

filenames = [os.path.join(a, x) for x in f]
w = csv.writer(open(a+"/"+'total.csv', 'w'))

for l in filenames :

    file = l.split('/')[1]
    if '.csv' not in l :
        x = open(l, 'r').readlines()
        for j in x:
            j = j.strip()
            # print(j)
            # print()
            # print()
            first = j.split('::')[0].strip()
            rest = j.split('::')[1].strip().split(' | ')
            data = [first]
            data.extend(rest)
            # print(data)
            print()
            print()
            if data != [] :
                # print(data[0])
                w.writerow(data)
        # print(total)
        # pass

    else :
        with open(l, 'r') as f:
            data = list(csv.reader(f))[1:]

        if data != [] :
            # print(data[0])
            for j in data :
                w.writerow(j)
