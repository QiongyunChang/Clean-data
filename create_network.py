import numpy as np
import csv
import pandas as pd
d =19

header = ['life sciences','physical sciences','computer science','engineering','arts and humanities','education','clinical and health','social sciences','psychology']
data = pd.read_csv('merge_data/merge.csv', keep_default_na=False)
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
with open('relation/relation_index.csv', 'w', newline='') as relation_file:
    for i in range(len(data)):
        top = data.iloc[i].sort_values(ascending=False)
        # print(list(top[:2].index))
        writer = csv.writer(relation_file)
        writer.writerow(list(top[:2].index))



def create_matrix(data):
    # Create two user-item matrices, one for training and another for testing
    data_matrix = np.zeros((len(data), len(data)))
    # print(np.shape(train_data))
    with open('relation/relation_index.csv', 'r', newline='') as f:
        reader = f.readlines()
        for line in reader:
            index = list(line)
            # bi-directional
            data_matrix[int(index[0]), int(index[2])] += 1
            data_matrix[int(index[2]), int(index[0])] += 1
    # print(data_matrix.astype(int))
    return data_matrix.astype(int)


result =create_matrix(header)
print(result)
mid_term_marks_df = pd.DataFrame(result)

mid_term_marks_df.to_csv("adjmatrix/adjmatrix.csv")

import networkx as nx
import matplotlib.pyplot as plt
from itertools import chain

G = nx.Graph()
for i in range(9):
    for j in range(9):
        # print(i,j,result[i,j])
        G.add_edge(i, j, color='b', weight=result[i,j])
        # G.add_edge(8, 9, color='b', weight=0.76)
pos = nx.circular_layout(G)
colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()
list_item=[]
# mean_wei=np.mean(np.array(weights))
for item in weights:
    list_item.append(item)

print(list_item)
norm = [float(i)/sum(list_item) for i in list_item]
# print(norm*10)
# print(norm)
norm = [i*0.003 for i in list_item]

# norm*=1000
# weights=np.array(weights)
# print(norm)
#
nx.draw(G, pos, edge_color=colors, width=list(norm),with_labels = True)


plt.show()
# plt.savefig("2000.png")

# libraries

# create adj matrix

