import streamlit as st
import functions



todos = functions.get_todos()

st.title("Welcome to my site!!!")
st.subheader("Below are a couple of things i've implemented so far!")

st.title("Squared calculator")
x = st.slider("This number squared is: ")
st.write(x, "squared is", x * x)
st.title("Find a color code")
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my ToDo App")
st.write("This app is for increasing your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new Todo...",
              on_change=add_todo, key='new_todo')
