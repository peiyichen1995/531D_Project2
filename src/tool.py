import pandas as pd
import numpy as np
def readData(file):
    data=pd.read_pickle(file)
    budgets=np.array(data[0]) #shape(n,)
    bids=np.array(data[1]) #shape(n,r)
    queries=np.array(data[2]) #shape(m,)
    # for first 3 datasets, the values in queries are the index of keyword such as 0,1
    return budgets,queries,bids
#readData('ds0.pkl')

def sortBids(bids):
    dict = {}
    for i in range(len(bids)):
        for j in range(len(bids[0])):
            if (bids[i][j] in dict):
                dict[bids[i][j]].append([i, j])
            else:
                dict[bids[i][j]] = [[i, j]]
    dict = sorted(dict.items())

    return dict
