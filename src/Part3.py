import numpy as np
from numpy import unravel_index
import math
from tool import *
import random

def extension2_1(budgets, queries, bids, e):
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
        total_bids = 0
        for i in range(n):
            total_bids+=bids[i][j]
        
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
        if t>e*m:
            for i in range(n):
                discount[i] = 1+math.exp(bids[i][j]/total_bids-1)-math.exp(M[imax]/budgets[imax]-1)
        #else no feasible solution for this query
        t+=1
    return selected, np.sum(M)   

def extension2(budgets, queries, bids, e):
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
        if t>e*m:
            for i in range(n):
                discount[i] = 1
        #else no feasible solution for this query
        t+=1
    return selected, np.sum(M)   

def extension4(budgets, queries, bids, threshold):
    n=len(budgets)
    m=len(queries)
    #Initialize M    
    M=np.zeros(n)
    # At first the time stamp is 0
    t=0
        
    while t < m :
        j=queries[t]
        maxBid=0
        maxId=-1
        for i in range(n):
            if(budgets[i]-M[i]>=bids[i][j] and bids[i][j]>maxBid):
                maxBid = bids[i][j]
                maxId = i
        
        # if the maximum bid is 0, no need to find the tie bid.
        if(maxBid==0): 
            t+=1
            continue
        presum = []
        presum.append((maxBid,maxId))
        for i in range(n):
            #choose the maximum bids within threshold
            if(budgets[i]-M[i]>=bids[i][j] and maxBid-bids[i][j]<threshold and i!=maxId):
                presum.append((bids[i][j]+presum[-1][0],i))
        
        rand = random.random()*presum[-1][0]
        # print(rand)
        currid=0
        for id, e in enumerate(presum):
            if rand < e[0]:
                currid=presum[id][1]
                M[currid]+=bids[currid][j]    
                break
        t+=1
    return np.sum(M)