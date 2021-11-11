import Part2,Part1
import tool
budgets, queries, bids=tool.readData('../data/ds2.pkl')
print(budgets.shape,queries.shape,bids.shape)
# Part2.LPOnlineAdWord(budgets, queries, bids,1)
Part1.naiveLPOfflineAdWord(budgets, queries, bids)