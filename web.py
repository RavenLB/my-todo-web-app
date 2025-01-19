import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    functions.write_json_todos(todos)

st.title("Mt todo list")
st.subheader("Tasks for today:")
##st.write("some more <b> text </b>", unsafe_allow_html=True) #making it bold

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_json_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="add a new task", placeholder= "Add a new todo",
               on_change=add_todo, key='new_todo')
