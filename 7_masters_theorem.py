import streamlit as st
import math

# https://www.gatevidyalay.com/masters-theorem-solving-recurrence-relations/

st.title("Recurance Relation - Masters Theorem")
st.header("Enter the parameters")

# a=st.number_input("Enter a: ",0)
a = int(st.text_input('a','0'))
b = int(st.text_input('b','0'))
k = int(st.text_input('k','0'))
p = int(st.text_input('p','0'))
sign = st.selectbox("sign",['+','-'])

st.header("Reccurance Relation is:")
temp = "T(n) = " + str(a) + "T(n/" + str(b) + ")" + sign + " theta(n^" + str(k) + " log^" + str(p) + "n)"
st.subheader(temp)
if a >= 1 and b > 1 and k >= 0 and sign == '+':
    st.header("The Time Complexity is: ")
    if a == pow(b,k):
        if(p > -1):
            # math.log(b*a)
            temp = "T(n) = theta(n^" + str(round(math.log2(a)/math.log2(b))) + " * log^" + str(p+1) + " n)"
        elif(p == -1):
            # math.log(b*a)
            temp = "T(n) = theta(n^" + str(round(math.log2(a)/math.log2(b))) + " * loglogn)"
        else:
            # math.log(b*a,2)
            temp = "T(n) = theta(n^" + str(round(math.log2(a)/math.log2(b))) + ")"
    elif a < pow(b,k):
        if p >= 0:
            temp = "T(n) = theta(n^" + str(k) + " log^" + str(p) + " n)"
        else:
            temp = "T(n) = theta(n^" + str(k) + ")"
    else:
            # math.log(b*a)
            temp = "T(n) = theta(n^" + str(math.log2(a)/math.log2(b)) + ")"
    st.subheader(temp)
else:
    st.subheader("Cannot solve the recurrence relation using master theorem")