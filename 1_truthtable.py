import pandas as pd
import streamlit as st

# st.write("Mathematical Computation Lab")
intro = '<p style="font-family:Arial; color:purple; font-size:32px;"> MATHEMATICAL COMPUTATION LAB </p>'
st.markdown(intro, unsafe_allow_html=True)

st.title("Equivalence Table for Gates")

n = st.number_input('Enter number of bits : ',min_value=1, max_value=100, value=5, step=1)
gates = st.radio("Select the Gate:",['AND','OR','NAND','NOR','XOR','XNOR'])

def table(n):
    if n<1:
        return [[]]
    subtable = table(n-1)
    return [row+[v] for row in subtable for v in [0,1]]

bits = table(n)

and_list = []
or_list = []
xor_list = []
xnor_list = []
nor_list = []
nand_list = []

if gates == 'AND':
    for i in range(len(bits)):
        AND = 1
        for j in range(n):
            AND &=bits[i][j]
        and_list.append(AND)
        
    df = pd.DataFrame(bits)
    df['table']=and_list
    

if gates == 'OR':
    for i in range(len(bits)):
        OR = 0
        for j in range(n):
            OR |=bits[i][j]
        or_list.append(OR)
        
    df = pd.DataFrame(bits)
    df['table']=or_list

if gates == 'NAND':
    for i in range(len(bits)):
        NAND = 1
        for j in range(n):
            NAND  &= bits[i][j]
        NAND = int(not(NAND))
        nand_list.append(NAND)
        
    df = pd.DataFrame(bits)
    df['table']=nand_list
    
if gates == 'NOR':
    for i in range(len(bits)):
        NOR = 0
        for j in range(n):
            NOR =(NOR | bits[i][j])
        NOR = int(not(NOR))
        nor_list.append(NOR)
        
    df = pd.DataFrame(bits)
    df['table']=nor_list

if gates == 'XOR':
    for i in range(len(bits)):
        XOR = 0
        for j in range(n):
            XOR ^=bits[i][j]
        xor_list.append(XOR)
        
    df = pd.DataFrame(bits)
    df['table']=xor_list

if gates == 'XNOR':
    for i in range(len(bits)):
        XNOR = 1 
        for j in range(n):
            XNOR ^=bits[i][j]
        xnor_list.append(XNOR)
        
    df = pd.DataFrame(bits)
    df['table']=xnor_list
    
st.table(df)
