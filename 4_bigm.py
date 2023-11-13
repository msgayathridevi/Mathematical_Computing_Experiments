import pulp as p  # import the library PuLP as p
import streamlit as st

st.title('LPP')
user_input = st.text_input("Enter maximize or minimize")
user_input.lower()

if user_input == "maximize":
    Lp_prob = p.LpProblem('Activity-Analysis_1 Maximize : ', p.LpMaximize)
else:
    Lp_prob = p.LpProblem('Activity-Analysis_1 Minimiza : ', p.LpMinimize)

# Set Up Problem Variables:
n = st.number_input("ENTER NUMBER OF PARAMETERS", 2, 4)

if n == 3:
    c = p.LpVariable("c", lowBound=0)  # "c" for chair
    t = p.LpVariable("t", lowBound=0)  # "t" for table
    d = p.LpVariable("d", lowBound=0)  # "d" for desk

    # Create Objective Function:
    st.write("Enter the objective function parameters")
    c1, c2, c3 = st.columns([1, 1, 1])
    n1 = c1.number_input("n1", step=1)
    n2 = c2.number_input("n2", step=1)
    n3 = c3.number_input("n3", step=1)
    
    Lp_prob += n1 * c + n2 * t + n3 * d

    # Create Constraints:
    Lp_prob += 3 * c + 1 * t + 4 * d <= 600
    Lp_prob += 2 * c + 4 * t + 2 * d >= 480
    Lp_prob += 2 * c + 3 * t + 3 * d == 540
    # Show the problem:
    st.write(Lp_prob)  # note that it's shown in alphabetical order
    # Solve the Problem:
    Lp_prob.solve()
    st.write(p.LpStatus[Lp_prob.status])

    # Printing Number of Chairs and Tables:
    for var in (c, t, d):
        st.write('Optimal number of {} to produce is: {:1.0f}'
                 .format(var.name, var.value()))
    # Printing the final solution
    st.write(p.value(Lp_prob.objective))