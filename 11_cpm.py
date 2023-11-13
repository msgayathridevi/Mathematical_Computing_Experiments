import streamlit as st
import networkx as nx

st.title("CPM")
n=int(st.number_input("Enter number of tasks",value=0))
task=[]
duration=[]

for i in range(n):
    tasks=st.text_input(f"Task {i+1}")
    durations=st.number_input(f"Duration {i+1}",value=1)
    task.append(tasks)
    duration.append(durations)

G=nx.DiGraph()

for i in range(n):
    G.add_node(task[i],duration=duration[i])

for i in range(n):
    dependencies=st.multiselect(f"Task {i+1} depend on",task[:i])
    for dependency in dependencies:
        G.add_edge(dependency,task[i])

path=nx.algorithms.dag.dag_longest_path(G)
length=nx.algorithms.dag.dag_longest_path_length(G)

st.write("Critical path is",path)
st.write("Total duration is",length)

