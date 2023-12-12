# Vogel Approximation Method

import streamlit as st
import pandas as pd
from pulp import *

def solve_vogels_approximation_method(supply, demand, costs):
    problem = LpProblem("Vogel's Approximation Method", LpMinimize)

    num_sources = len(supply)
    num_destinations = len(demand)
    variables = []

    for i in range(num_sources):
        row = []
        for j in range(num_destinations):
            variable = LpVariable(f"source_{i}destination{j}", 0, None, LpInteger)
            row.append(variable)
        variables.append(row)

    # Define the objective function
    objective = []
    for i in range(num_sources):
        for j in range(num_destinations):
            objective.append(variables[i][j] * costs[i][j])
    problem += lpSum(objective)

    # Define the supply constraints
    for i in range(num_sources):
        problem += lpSum(variables[i]) == supply[i]

    # Define the demand constraints
    for j in range(num_destinations):
        problem += lpSum([variables[i][j] for i in range(num_sources)]) == demand[j]

    problem.solve()

    solution = []
    for i in range(num_sources):
        row = []
        for j in range(num_destinations):
            row.append(variables[i][j].value())
        solution.append(row)
        
    return solution, value(problem.objective)


st.title("Vogel's Approximation Method")
import numpy as np
sup=int(st.number_input("Enter no.of (supply/source):"))
dmd=int(st.number_input("Enter no.of (demand/destination):"))
st.write("Enter costs one by one ")

entries=[] 
supply=[]
demand=[]
for i in range(0,sup*dmd):
    d1 = (st.number_input("Enter cost for jobs ",key=i))
    entries.append(int(d1))
costs = np.array(entries).reshape(sup, dmd)
st.write(costs)

for i in range(0,sup):
    d2=st.number_input("Enter supply values: ",i)
    supply.append(int(d2))
st.write(supply)

for i in range(0,dmd):
    d3=st.number_input("Enter demand values:",i)
    demand.append(int(d3))
st.write(demand)

transportation_matrix, objective = solve_vogels_approximation_method(supply, demand, costs)

df = pd.DataFrame(transportation_matrix, columns=[f"Destination {j}" for j in range(len(demand))])
df.index = [f"Source {i}" for i in range(len(supply))]
st.write("Transportation Matrix:")
st.write(df)

st.write("Total Cost:", objective)