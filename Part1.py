import numpy as np
from numpy import unravel_index
from scipy.optimize import linprog

def greedyOfflineAdWord(budgets, queries, bids):
    n = len(budgets)
    m = len(queries)

    # Initialize M
    M = np.zeros(n)

    # at the start, no one is sold
    sold = np.zeros(m)

    ans = []
    while(np.sum(bids) > 0):
        (i, j) = unravel_index(bids.argmax(), bids.shape)

        if (sold[j] == 0):
            if (0 < bids[i][j] and bids[i][j] <= budgets[i] - M[i]):
                M[i] += bids[i][j]
                sold[j] = 1
                # Report the selected advertiser (if any) for each query with total revenue
                ans.update({j : i})

    return ans, np.sum(M)


def naiveLPOfflineAdWord():

    ans = []

    return ans
