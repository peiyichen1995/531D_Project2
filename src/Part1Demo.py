from Part1 import *
from gen import *

# print the selected bids for AdWord problem
def printSelectedBids(selected):
    for key in selected:
        print("Budget " + str(key) + ":")
        print(selected[key])
        print('\n')

# run experiment
def run_exp(file_name, id):
    print("Run each offline algorithm on the four provided datasets "+id+":\n")

    print('==================================================')
    print('==================================================\n')

    budgets, queries, bids = readData(file_name)
    print("Budget " + id +":")
    print(budgets)
    print("Queries " + id +":")
    print(queries)
    print("Bids " + id +":")
    print(bids)

    print('\n')
    print('Running greedyOfflineAdWord...')
    print('\n')

    selected, sum = greedyOfflineAdWord(budgets, queries, bids)

    print("Selected advertiser (if any) for each query: (query: selected advertiser)")
    printSelectedBids(selected)
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
    printSelectedBids(selected)
    print('\n')
    print("Total revenue: ")
    print(sum)

# budgets, queries, bids = readData('../data/ds0.pkl')
# print(bids)

print("================================= Showcase for part A ========================================")
ds_exp = ds0_gen(2)
dump('../data/ds_exp', ds_exp)
run_exp('../data/ds_exp.pkl', 'showcase')

print("================ Run each offline algorithm on the four provided datasets ==================")

run_exp('../data/ds0.pkl', '0')
run_exp('../data/ds1.pkl', '1')
run_exp('../data/ds2.pkl', '2')
run_exp('../data/ds3.pkl', '3')
