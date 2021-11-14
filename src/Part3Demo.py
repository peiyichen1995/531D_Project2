from Part3 import *
from Part2 import *
import tool
budgets, queries, bids=tool.readData('../data/ds3.pkl')
print(budgets.shape,queries.shape,bids.shape)
temp=extension4(budgets, queries, bids,0.02)
print(temp)
print()
print(greedyOnlineAdWord(budgets, queries, bids)[1])
