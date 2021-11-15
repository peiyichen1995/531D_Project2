import Part2
import tool
import numpy as np

def randomShuffling(ds,AdwordFun,e):
    revenues=np.zeros(100)
    budgets, queries, bids=tool.readData(ds)
    for i in range(100):
        np.random.shuffle(queries)
        revenues[i]=AdwordFun(budgets, queries, bids,e)[1]
    rev_average=np.average(revenues)
    rev_std=np.std(revenues)
    return rev_average,rev_std


def test100():
    res=[]
    for e in [0.05,0.1,0.2]:
        
        res.append(randomShuffling('../data/ds0.pkl', Part2.LPOnlineAdWord, e))
        res.append(randomShuffling('../data/ds1.pkl', Part2.LPOnlineAdWord, e))
        res.append(randomShuffling('../data/ds2.pkl', Part2.LPOnlineAdWord, e))
        res.append(randomShuffling('../data/ds3.pkl', Part2.LPOnlineAdWord, e))
    print(res)
# randomShuffling('../data/ds1.pkl', Part2.LPOnlineAdWord)
def testUnshuffle():
    res=[]
    for e in [0.05,0.1,0.2]:
        
        budgets, queries, bids=tool.readData('../data/ds0.pkl')
        res.append(Part2.LPOnlineAdWord(budgets, queries, bids,e)[1])
        budgets, queries, bids=tool.readData('../data/ds1.pkl')
        res.append(Part2.LPOnlineAdWord(budgets, queries, bids,e)[1])
        budgets, queries, bids=tool.readData('../data/ds2.pkl')
        res.append(Part2.LPOnlineAdWord(budgets, queries, bids,e)[1])
        budgets, queries, bids=tool.readData('../data/ds3.pkl')
        res.append(Part2.LPOnlineAdWord(budgets, queries, bids,e)[1])
    print(res)

budgets, queries, bids=tool.readData('../data/ds2.pkl')
np.random.shuffle(queries)
print(Part2.LPOnlineAdWord(budgets, queries, bids,0.1))