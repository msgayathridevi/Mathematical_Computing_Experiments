import streamlit as st
import numpy as np
from scipy.optimize import linear_sum_assignment

def assignment_problem(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix) #check hungarian , and balanced in note, formatting
    total_cost = cost_matrix[row_ind, col_ind].sum() ######
    return row_ind, col_ind, total_cost

# Set up the Streamlit app
st.title("Assignment Problem Solver")

# Get the number of rows and columns
n_rows = st.number_input("Number of rows", min_value=1, step=1)
n_cols = st.number_input("Number of columns", min_value=1, step=1)

# Get the cost matrix
cost_matrix = []
for i in range(n_rows):
    row = st.text_input(f"Row {i+1} costs (separated by spaces)", key=f"row_{i}")
    row = [int(x) for x in row.split()] ######

    if len(row) != n_cols:
        st.error(f"Row {i+1} must have exactly {n_cols} costs")
        cost_matrix = None ######
        break

    cost_matrix.append(row)

# If the cost matrix is valid, solve the assignment problem
if cost_matrix is not None:
    cost_matrix = np.array(cost_matrix)
    row_ind, col_ind, total_cost = assignment_problem(cost_matrix)
    
    # Display the results
    st.write("Optimal assignment:")
    for i, j in zip(row_ind, col_ind):
        st.write(f"Row {i+1} -> Column {j+1}")
    st.write(f"Total cost: {total_cost}")