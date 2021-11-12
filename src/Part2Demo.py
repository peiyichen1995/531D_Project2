import Part2,Part1
import tool
budgets, queries, bids=tool.readData('../data/ds1.pkl')
print(budgets.shape,queries.shape,bids)
temp=Part2.LPOnlineAdWord(budgets, queries, bids,0.5)
print(temp[1])
print(Part2.greedyOnlineAdWord(budgets, queries, bids)[1])