# check with sample observations

import streamlit as st
import numpy as np
from scipy.optimize import linprog

def simplex(c, A, b, maximize=True):
    # Convert the problem to the standard form
    if maximize:
        c = -c
    A = np.concatenate((A, np.eye(len(b))), axis=1)
    c = np.concatenate((c, np.zeros(len(b))))
    bounds = [(0, None) for i in range(len(c))]
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="simplex")
    # Convert the solution back to the original form
    x = res.x[:len(c)-len(b)]
    obj = -res.fun if maximize else res.fun
    return x, obj

st.title("Simplex algorithm")

m = st.slider("Number of constraints", min_value=1, max_value=5, value=2, step=1)
n = st.slider("Number of variables", min_value=1, max_value=5, value=2, step=1)
c = np.array([st.number_input(f"Objective coefficient {j+1}", value=0, step=1) for j in range(n)])
A = np.array([[st.number_input(f"Coefficient {i+1},{j+1}", value=0, step=1) for j in range(n)] for i in range(m)])
b = np.array([st.number_input(f"Right-hand side {i+1}", value=0, step=1) for i in range(m)])
maximize = st.checkbox("Maximize")

x, obj = simplex(c, A, b, maximize)
st.write("Solution:")
for j in range(n):
    st.write(f"x{j+1} = {x[j]}")
st.write(f"Objective value: {obj}")

