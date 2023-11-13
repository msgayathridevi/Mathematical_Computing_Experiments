import streamlit as st

st.title("Recursion : Josephuses Problem")
n=int(st.number_input("n : "))
k=int(st.number_input("k : "))

def Josh(person, k, index):
   
  if len(person) == 1:
    print("Last Left Out Person : ",person[0])
    st.write("Alive Person : ",person[0])
    return

  index = ((index+k)%len(person))
  person.pop(index)
  Josh(person,k,index)
 
k-=1  
index = 0
person=[]
for i in range(1,n+1):
  person.append(i)
 
if st.button("Answer"):
  Josh(person,k,index)

