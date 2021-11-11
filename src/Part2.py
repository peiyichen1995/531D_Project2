import numpy as np
from numpy import unravel_index
import math
from tool import *


# input: 
# budgets: a (n,) ndarray
# queries: a (m,) ndarray
# bids: a (n,r) ndarray n advertisers bid xxxx on r keywords
# return: 
# selected is a dictionary: a matching of advertisers and queries
# key-value example of selected: 
# i : [q1,q2,q3](a list of queries matched to i-th adverisers)
def greedyOnlineAdWord(budgets, queries, bids):
    n=len(budgets)
    m=len(queries)
    #Initialize M    
    M=np.zeros(n)
    # At first the time stamp is 0
    t=0
    # Initialize an empty selected dict
    selected={}
    # the timestamp is from 0 to m-1
    while t < m :
        j=queries[t]
        bidsmax=-1
        imax=-1
        for i in range(n):
            # if the adveriser doesn't bid, continue 
            if(bids[i][j]==0):
                continue
            #choose the maximum bids
            if(budgets[i]-M[i]>=bids[i][j]):
                if(bidsmax < bids[i][j]):
                    imax = i
                    bidsmax = bids[i][j]
        # exists a feasible matching for the t-th query
        if(imax != -1):
            if(imax in selected):
                selected[imax].append(t)
            else:
                selected[imax]=[t]
            M[imax]+=bids[imax][j]
        #else no feasible solution for this query
        t+=1
    return selected, np.sum(M), M

def weightedgreedyOnlineAdWord(budgets, queries, bids):
    n=len(budgets)
    m=len(queries)
    #Initialize M    
    M=np.zeros(n)
    discount=np.ones(n)
    # At first the time stamp is 0
    t=0
    # Initialize an empty selected dict
    selected={}
    # the timestamp is from 0 to m-1
    while t < m :
        j=queries[t]
        bidsmax=-1
        imax=-1
        for i in range(n):
            if(bids[i][j]==0):
                continue
            #choose the maximum weighted bids
            if(budgets[i]-M[i]>=bids[i][j]):
                if(bidsmax < discount[i]*bids[i][j]):
                    imax = i
                    bidsmax = discount[i]*bids[i][j]
        # exists a feasible matching for the t-th query
        if(imax != -1):
            if(imax in selected):
                selected[imax].append(t)
            else:
                selected[imax]=[t]
            M[imax]+=bids[imax][j]
            discount[imax]=1-math.exp(M[imax]/budgets[imax]-1)
        #else no feasible solution for this query
        t+=1
    return selected, np.sum(M)   

def LPOnlineAdWord(budgets, queries, bids, e):

    n = len(budgets)
    m = len(queries)

    # Initialize M
    t=int(e*m)
    pre_queries = queries[0:t]
    _,_,M = greedyOnlineAdWord(budgets, pre_queries, bids)
    print(np.sum(M))
    print("Compute an optimal fractional solution alpha*,beta* to the LP")
    print("----------------------------------------------------")
    # compute optimal fractional solution
    alpha = solveDualLP(budgets, pre_queries, bids, e)
    print("----------------------------------------------------")
    
    selected={}
    # the timestamp is from 0 to m-1
    t+=1
    while t < m :
        j=queries[t]
        bidsmax=-1
        imax=-1
        for i in range(n):
            if(bids[i][j]==0):
                continue
            #choose the maximum weighted bids
            if(budgets[i]-M[i]>=bids[i][j]):
                if(bidsmax < (1-alpha[i])*bids[i][j]):
                    imax = i
                    bidsmax = (1-alpha[i])*bids[i][j]
        # exists a feasible matching for the t-th query
        if(imax != -1):
            if(imax in selected):
                selected[imax].append(t)
            else:
                selected[imax]=[t]
            M[imax]+=bids[imax][j]
        #else no feasible solution for this query
        t+=1
    print(np.sum(M))
    return selected, np.sum(M)