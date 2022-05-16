import numpy as np
import csv
import pandas as pd
# header = ['social sciences','engineering','computer science','life sciences','psychology','physical sciences','arts and humanities','education','clinical and health']
data = pd.read_csv('merge.csv', keep_default_na=False)
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

with open('relation.csv', 'w', newline='') as relation_file:
    for i in range(len(data)):
        top = data.iloc[i].sort_values(ascending=False)
        # print(list(top[:2].index))
        writer = csv.writer(relation_file)
        writer.writerow(list(top[:2].index))
