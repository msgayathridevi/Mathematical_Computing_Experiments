import streamlit as st
import numpy as np
import pandas as pd
from scipy.optimize import linprog

st.title("Simplex Method")
st.write("Check the checkbox for maximixation problem")
maxi=st.checkbox("Maximization")

c=st.text_input("Enter objective function (split by ',')").split(",")

for i in range(len(c)):
    c[i]=int(c[i])
c=np.array(c)

if maxi:
    # c*=-1
    c=-c
else:
    c=c

nums_eq=st.number_input("Enter num of constraint:",min_value=2,max_value=10,key="0x")

a_ub=[]
b_ub=[]

for i in range(nums_eq):
    ineq = st.text_input("Enter constraints:",key="{}".format(i)).split(",")
    a_ub.append(ineq)

sol=st.text_input("Enter solution:").split(",")
b_ub=sol

bounds=[]
for i in range(len(c)):
    bounds.append((0,None))

res=linprog(c,A_ub=a_ub,b_ub=b_ub,bounds=bounds,method='simplex') # options={"disp":True})

if maxi:
    st.write("Objective={}".format(res.get('fun')*-1))
else:
    st.write("Objective={}".format(res.get('fun')*-1))
    
st.write("Optimal value={}".format(res.get('x')))
st.write(res['message'])
st.write(res)