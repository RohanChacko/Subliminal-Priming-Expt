import csv
import matplotlib.pyplot as plt
import numpy as np

csv_path = 'ExperimentalGroup/Aggregated Results - Experimental.csv'
with open(csv_path, 'r') as f:
        data = list(csv.reader(f))


# All headers for the csv file
head = data[0][:-2]
head = [x for x in head if x!='' ]

# Extracting relevant cols from header
headers = [head[0], head[2]]
headers.extend(head[-2:])

# Extracting relevant cols from data rows
data = data[2:-3]
data = [x[:-2] for x in data]
rows = [[x[0], x[2]] for x in data]

color_prime_count = {'red': 0, 'orange': 0, 'yellow': 0, 'green': 0, 'blue': 0, 'purple': 0, 'black': 0}
color_count = {'red': 0, 'orange': 0, 'yellow': 0, 'green': 0, 'blue': 0, 'purple': 0, 'black': 0}
prime_count = 0

for i in range(len(rows)) :
    rows[i].extend(data[i][-2:])
    rows[i][0] = int(rows[i][0])
    rows[i][2] = int(rows[i][2])

    # if rows[i][1] == 0 :
    #     time_0.append(rows[i])
    #     if rows[i][2] == 'T' :
    #         count_0 += 1
    # elif rows[i][1] == 120 :
    #     time_120.append(rows[i])
    #     if rows[i][2] == 'T' :
    #         count_120 += 1
    # elif rows[i][1] == 300 :
    #     time_300.append(rows[i])
    #     if rows[i][2] == 'T' :
    #         count_300 += 1
    # else :
    #     pass

    if rows[i][3] == 'T' :
        prime_count += 1
        color_prime_count[rows[i][1]] +=1

    color_count[rows[i][1]] +=1

# print(headers)
# print(rows)
for i in color_prime_count.keys() :
    color_prime_count[i] = 100 * color_prime_count[i] / color_count[i]

plt.figure(figsize=(10, 10))
plt.title('Experimental Group Results for each color')
# y = [count_0/len(time_0)*100, count_120/len(time_120)*100, count_300/len(time_300)*100]
# x = ['0s', '120s', '300s']

plt.xlabel('Colors used for priming')
plt.ylabel('No. of people primed ')
plt.ylim([0,40])
plt.yticks(np.arange(0, max(color_count.values())+10, 4.0))

plt.bar(color_count.keys(), color_count.values(), width=0.4, color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'])
for i, v in enumerate(color_count.keys()):
    plt.text(i -.4, color_count[v] + .25, str(f'{color_count[v]:9.0f}'), color='black', fontweight='bold')

plt.savefig('Experimental_Group_Color_Part1.png', bbox='tight')
plt.show()
