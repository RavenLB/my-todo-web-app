import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    functions.write_json_todos(todos)

st.title("Lidl shopping list for Constant")
st.subheader("cinnamon roll ingredients missing:")
##st.write("some more text")

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_json_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="add a new ingredient", placeholder= "Add a new todo",
               on_change=add_todo, key='new_todo')
