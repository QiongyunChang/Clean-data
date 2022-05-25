import pandas as pd
import numpy as np

import numpy as np
import csv
import pandas as pd
import csv
header = ['life sciences','physical sciences','computer science','engineering','arts and humanities','education','clinical and health','social sciences','psychology']
data = pd.read_csv('2000.csv', keep_default_na=False)
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
# print(data)
array = []

from itertools import combinations

with open('top3_2000.csv', 'w', newline='') as relation_file:
    for i in range(len(data)):
        writer = csv.writer(relation_file,delimiter=',')
        top = data.iloc[i].sort_values(ascending=False)
        # # top3 = (top[0].index)+(top[1].index)+(top[2].index)
        top3 =map(int,list(top[:3].index))
        # writer.writerow([total])
        temp = combinations(top3, 2)
        writer.writerow(temp)



def create_matrix(header):
    # Create two user-item matrices, one for training and another for testing
    data_matrix = np.zeros((len(header), len(header)))
    # print(np.shape(train_data))
    with open('top3_2000.csv', 'r', newline='') as f:
        reader = f.readlines()
        specialChars = "!#$%^&*(),+\ \r\n "" "
        for line in reader:
            for specialChar in specialChars:
                line=line.replace(specialChar, '')
            index = list(line)
            # bi-directional
            data_matrix[int(index[1]), int(index[2])] += 1
            data_matrix[int(index[5]), int(index[6])] += 1
            data_matrix[int(index[9]), int(index[10])] += 1
            data_matrix[int(index[2]), int(index[1])] += 1
            data_matrix[int(index[6]), int(index[5])] += 1
            data_matrix[int(index[10]), int(index[9])] += 1
    print(data_matrix.astype(int))
    return data_matrix.astype(int)

result = create_matrix(header)
mid_term_marks_df = pd.DataFrame(result)
mid_term_marks_df.to_csv("top3_adj_2000.csv")
print("END")

''' # FOR PROPOTION 
half = [0,0,0,0,0,0,0,0,0]
for i in range(len(data)):
    # writer = csv.writer(relation_file,delimiter=',')
    top = data.iloc[i].sort_values(ascending=False)
    summ =list(map(float,top[:3]))
    total = sum(summ)
    if total >= 0.1 and total < 0.2:
        half[0] += 1
    if total >= 0.2 and total < 0.3:
        half[1] += 1
    if total >= 0.3 and total < 0.4:
        half[2] += 1
    if total >= 0.4 and total < 0.5:
        half[3] += 1
    if total >= 0.5 and total < 0.6:
        half[4]+=1
    if total >= 0.6 and total < 0.7:
        half[5] += 1
    if total >= 0.7 and total < 0.8:
        half[6] += 1
    if total >= 0.8 and total < 0.9:
        half[7] += 1
    if total >= 0.9:
        half[8] += 1


print(half)

summm = sum(half)
propotion = [j/summm for j in half]
print(propotion)'''


