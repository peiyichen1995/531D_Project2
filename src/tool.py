import pandas as pd
import numpy as np
from pulp import *


def readData(file):
    data=pd.read_pickle(file)
    budgets=np.array(data[0]) #shape(n,)
    bids=np.array(data[1]) #shape(n,r)
    queries=np.array(data[2]) #shape(m,)
    # for first 3 datasets, the values in queries are the index of keyword such as 0,1
    return budgets,queries,bids
#readData('ds0.pkl')

# sort bids according to bid value, saved in dictionary w_ij : [i, j]
def sortBids(bids):
    dict = {}
    for i in range(len(bids)):
        for j in range(len(bids[0])):
            if (bids[i][j] in dict):
                dict[bids[i][j]].append([i, j])
            else:
                dict[bids[i][j]] = [[i, j]]
    dict = sorted(dict.items())

    return dict

def solveLP(budgets, queries, bids):
    # create a list of all the budgets
    # Creates a dictionary for the number of units of budget for each budgets
    B_names = []
    Bs = {}
    for i in range(len(budgets)):
        B_names.append("B"+str(i))
        Bs["B"+str(i)] = budgets[i]

    q_names = []
    qs = {}
    # Creates a list of all queries
    for i in range(len(queries)):
        q_names.append(str(i))
        qs[str(i)] = str(queries[i])

    n = len(budgets)
    m = len(queries)
    t_bids = np.zeros((n, m))
    for i in range(len(budgets)):
        for t in range(len(queries)):
            t_bids[i][t] = bids[i][queries[t]]

    # The bids data is made into a dictionary
    costs = makeDict([B_names,q_names],t_bids,0)

    # Creates the 'prob' variable to contain the problem data
    prob = LpProblem("AdWord Problem",LpMaximize)

    # Creates a list of tuples containing all the possible routes for transport
    Routes = [(w,b) for w in B_names for b in q_names]

    # A dictionary called 'Vars' is created to contain the referenced variables(the routes)
    vars = LpVariable.dicts("Route",(B_names,q_names),0,None,cat='Continuous')

    # The objective function is added to 'prob' first
    prob += lpSum([vars[w][b]*costs[w][b] for (w,b) in Routes]), "Sum_of_Total_Revenue"

    # The supply maximum constraints are added to prob for each supply node (warehouse)
    for w in B_names:
        prob += lpSum([vars[w][b]*costs[w][b] for b in q_names])<=Bs[w], "Sum_of_Products_out_of_Budget_%s"%w

    # The demand minimum constraints are added to prob for each demand node (bar)
    for b in q_names:
        prob += lpSum([vars[w][b] for w in B_names])<=1, "Sum_of_Bids_into_Query%s"%b

    # The problem data is written to an .lp file
    prob.writeLP("AdWordProblem.lp")

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The status of the solution is printed to the screen
    print( "Status:", LpStatus[prob.status])

    frac_x = {}
    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
        if (v.varValue != 0):
            # print (v.name, "=", v.varValue)
            name_split = (v.name).split('_')
            if (v.varValue in frac_x):
                frac_x[v.varValue].append([int(name_split[1][1:]), int(name_split[2])])
            else:
                 frac_x[v.varValue] = [[int(name_split[1][1:]), int(name_split[2])]]

    # The optimised objective function value is printed to the screen
    print ("Total Revenue = ", value(prob.objective))

    return sorted(frac_x.items())

def solveDualLP(budgets, queries, bids, e):
    # create a list of all the budgets
    # Creates a dictionary for the number of units of budget for each budgets
    n = len(budgets)
    B_names = []
    Bs = {}
    for i in range(len(budgets)):
        B_names.append(str(i))
        Bs[str(i)] = budgets[i]

    q_names = []
    qs = {}
    # Creates a list of all queries
    
    for i in range(len(queries)):
        q_names.append(str(i))
        qs[str(i)] = str(queries[i])
    # The bids data is made into a dictionary
    costs = makeDict([B_names,q_names],bids,0)

    # Creates the 'prob' variable to contain the problem data
    prob = LpProblem("AdWord Dual Problem",LpMinimize)

   

    # Dictionary called alpha and beta are created to contain the referenced variables(the routes)
    alpha = LpVariable.dicts("alpha",(B_names),0,None,cat='Continuous')
    beta = LpVariable.dicts("beta",(q_names),0,None,cat='Continuous')

    # The objective function is added to 'prob' first
    prob += (lpSum([e*alpha[w]*Bs[w] for w in B_names]+[beta[b] for b in q_names])), "Dual"

    # Creates a list of tuples containing all the possible routes for transport
    Routes = [(w,b) for w in B_names for b in q_names]
    for (w,b) in Routes:
        # w=r[0],b=r[1]
        prob += alpha[w]*costs[w][qs[b]]+beta[b]>=costs[w][qs[b]], "Constraint (%s,%s)"%(w,b)

    # The problem data is written to an .lp file
    prob.writeLP("AdWordProblem.lp")

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The status of the solution is printed to the screen
    print( "Status:", LpStatus[prob.status])
    
    # Each of the variables is printed with it's resolved optimum value
    res=np.zeros(n)
    for v in prob.variables():
        if (v.varValue != 0):
            name_split = (v.name).split('_')
            
            if(name_split[0]=="alpha"):
                print (v.name, "=", v.varValue)
                res[int(name_split[1])]=v.varValue

    return res