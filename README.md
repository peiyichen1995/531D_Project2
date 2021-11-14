# Algorithms for Sponsored Keyword Search
- This is the second course project for Duke University's Compsci 531D Fall21.

### Required Packages:
- numpy
- scipy.optimize
- matplotlib.pyplot
- math

### Part 1:

Description:
- selected, total revenue = greedyOfflineAdWord(budgets, queries, bids)
  * budgets is a one-dimensional ndarray, shape(n,)
  * queries is  a one-dimensional ndarray, shape(m,)
  * bids is a two-dimensional ndarray, shape(n,r)
  * selected: a list of queries matched to i-th adverisers, below is a key-value example:
  * i : [q1,q2,q3], [q1,q2,q3] is a list of queries matched to i-th adverisers 

- selected, total revenue = naiveLPOfflineAdWord(budgets, queries, bids)
  * budgets is a one-dimensional ndarray, shape(n,)
  * queries is  a one-dimensional ndarray, shape(m,)
  * bids is a two-dimensional ndarray, shape(n,r)
  * selected: a list of queries matched to i-th adverisers, below is a key-value example:
  * i : [q1,q2,q3], [q1,q2,q3] is a list of queries matched to i-th adverisers 

Usage:
- from Part1 import *
- Run 'python Part1Demo.py' for slides results

### Part 2:

Description:

* selected, total revenue = greedyOnlineAdWord(budgets, queries, bids)
  * budgets is a one-dimensional ndarray, shape(n,)
  * queries is  a one-dimensional ndarray, shape(m,)
  * bids is a two-dimensional ndarray, shape(n,r)
  * selected: a list of queries matched to i-th adverisers, below is a key-value example:
  * i : [q1,q2,q3], [q1,q2,q3] is a list of queries matched to i-th adverisers 
* selected, total revenue = weightedgreedyOnlineAdWord(budgets, queries, bids)
  - budgets is a one-dimensional ndarray, shape(n,)
  - queries is  a one-dimensional ndarray, shape(m,)
  - bids is a two-dimensional ndarray, shape(n,r)
  - selected: a list of queries matched to i-th adverisers, below is a key-value example:
  - i : [q1,q2,q3], [q1,q2,q3] is a list of queries matched to i-th adverisers

### tools

* budgets,queries,bids=readData(file)
  * budgets,queries,bids are ndarrays
  * this function is suitable for ds0-ds2

