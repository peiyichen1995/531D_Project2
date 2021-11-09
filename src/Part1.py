import numpy as np
from scipy.optimize import linprog
from tool import *

def greedyOfflineAdWord(budgets, queries, bids):
    n = len(budgets)
    m = len(queries)

    # Initialize M
    M = np.zeros(n)

    # at the start, no one is sold
    sold = np.zeros(m)

    selected = {}
    dict = sortBids(bids)
    for k in range(len(dict)-1, -1, -1):
        for l in range(len(dict[k][1])):
            i = dict[k][1][l][0]
            j = dict[k][1][l][1]

            if (sold[j] == 0):
                if (0 < bids[i][j] and bids[i][j] <= budgets[i] - M[i]):
                    M[i] += bids[i][j]
                    sold[j] = 1
                    # Report the  advertiser (if any) for each query with total revenue
                    selected[j] = i

    return selected, np.sum(M)


def naiveLPOfflineAdWord(budgets, queries, bids):

    n = len(budgets)
    m = len(queries)

    # Initialize M
    M = np.zeros(n)

    # at the start, no one is sold
    sold = np.zeros(m)

    print("Compute an optimal fractional solution x∗ to the LP")
    print("----------------------------------------------------")
    # compute optimal fractional solution
    dict = solveLP(budgets, queries, bids)
    print("----------------------------------------------------")


    # selected = {}
    # dict = sortBids(bids)
    # while(np.sum(x) > 0):
    #     (i, j) = unravel_index(x.argmax(), x.shape)
    #
    #     if (sold[j] == 0):
    #         if (0 < bids[i][j] and bids[i][j] <= budgets[i] - M[i]):
    #             M[i] += bids[i][j]
    #             sold[j] = 1
    #             # Report the  advertiser (if any) for each query with total revenue
    #             selected[j] = i

    selected = {}
    for k in range(len(dict)-1, -1, -1):
        for l in range(len(dict[k][1])):
            i = dict[k][1][l][0]
            j = dict[k][1][l][1]

            if (sold[j] == 0):
                if (0 < bids[i][j] and bids[i][j] <= budgets[i] - M[i]):
                    M[i] += bids[i][j]
                    sold[j] = 1
                    # Report the  advertiser (if any) for each query with total revenue
                    selected[j] = i


    return selected, np.sum(M)
