from Part1 import *

# a = np.bids_0ay([[10,50,30],[60,20,40]])
# (i, j) = unravel_index(a.argmax(), a.shape)
# print(np.sum(a))

budgets_0, queries_0, bids_0 = readData('../data/ds0.pkl')
print("Budget 0: ")
print(budgets_0)
print("Queries 0: ")
print(queries_0)
print("Bids 0: ")
print(bids_0)

print('\n')
print('Running greedyOfflineAdWord...')
print('\n')

selected_0, sum_0 = greedyOfflineAdWord(budgets_0, queries_0, bids_0)
print("Selected advertiser (if any) for each query: (query: selected advertiser)")
print(selected_0)
print('\n')
print("Total revenue: ")
print(sum_0)

print('==================================================\n')
