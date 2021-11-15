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

  selected is a dictionary map each query to its selected bid

- selected, total revenue = naiveLPOfflineAdWord(budgets, queries, bids)

  selected is a dictionary map each query to its selected bid

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
* total revenue = LPOnlineAdWord(budgets, queries, bids, e)
  - budgets is a one-dimensional ndarray, shape(n,)
  - queries is  a one-dimensional ndarray, shape(m,)
  - bids is a two-dimensional ndarray, shape(n,r)
  - e is a threshold for learning process

### Part 3:
* selected, total revenue = extension2(budgets, queries, bids, e)
  - budgets is a one-dimensional ndarray, shape(n,)
  - queries is  a one-dimensional ndarray, shape(m,)
  - bids is a two-dimensional ndarray, shape(n,r)
  - selected: a list of queries matched to i-th adverisers, below is a key-value example:
  - e is a threshold. Before e, it is the same as weighted-online learning. After e, it choose based on bid.
* total revenue = extension4(budgets, queries, bids, threshold):
  - budgets is a one-dimensional ndarray, shape(n,)
  - queries is  a one-dimensional ndarray, shape(m,)
  - bids is a two-dimensional ndarray, shape(n,r)
  - threshold define the maximum difference between choosen bid and maximum bid.
  
Description:
### tools

* budgets,queries,bids=readData(file)
  * budgets,queries,bids are ndarrays
  * this function is suitable for ds0-ds2

