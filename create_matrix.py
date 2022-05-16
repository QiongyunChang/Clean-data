import numpy as np
import csv
import pandas as pd
header = ['social sciences','engineering','computer science','life sciences','psychology','physical sciences','arts and humanities','education','clinical and health']
data = pd.read_csv('merge.csv', keep_default_na=False)
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

'''
with open('relation_index.csv', 'w', newline='') as relation_file:
    for i in range(len(data)):
        top = data.iloc[i].sort_values(ascending=False)
        # print(list(top[:2].index))
        writer = csv.writer(relation_file)
        writer.writerow(list(top[:2].index))
'''



def create_matrix(data):
    # Create two user-item matrices, one for training and another for testing
    data_matrix = np.zeros((len(data), len(data)))
    # print(np.shape(train_data))
    with open('relation_index.csv', 'r', newline='') as f:
        reader = f.readlines()
        for line in reader:
            index = list(line)
            # bi-directional
            # print(data_matrix)
            data_matrix[int(index[0]), int(index[2])] += 1
            data_matrix[int(index[2]), int(index[0])] += 1
    print(data_matrix.astype(int))


