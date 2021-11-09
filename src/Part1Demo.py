from Part1 import *

def run_exp(file_name, id):
    print("Run each offline algorithm on the four provided datasets "+str(id)+":\n")

    print('==================================================')
    print('==================================================\n')

    budgets, queries, bids = readData(file_name)
    print("Budget 0: ")
    print(budgets)
    print("Queries 0: ")
    print(queries)
    print("Bids 0: ")
    print(bids)

    print('\n')
    print('Running greedyOfflineAdWord...')
    print('\n')

    selected, sum = greedyOfflineAdWord(budgets, queries, bids)

    print("Selected advertiser (if any) for each query: (query: selected advertiser)")
    print(selected)
    print('\n')
    print("Total revenue: ")
    print(sum)
    print('\n')
    print('==================================================\n')

    print('Running naiveLPOfflineAdWord...')
    print('\n')

    selected, sum = naiveLPOfflineAdWord(budgets, queries, bids)

    print('\n')
    print("Selected advertiser (if any) for each query: (query: selected advertiser)")
    print(selected)
    print('\n')
    print("Total revenue: ")
    print(sum)

run_exp('../data/ds0.pkl', 0)
run_exp('../data/ds1.pkl', 1)
run_exp('../data/ds2.pkl', 2)
run_exp('../data/ds3.pkl', 3)
