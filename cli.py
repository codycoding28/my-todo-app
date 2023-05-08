from functions import get_todos, write_todos
import time

# implementing time feature

now = time.strftime("%b, %d, %Y, %H:%M:%S")
print("It is", now)
user_prompt = "Type add, show, complete, edit or exit: "

while True:
    # get user input and strip space characters from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    # check if user action is "add"
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos, "todos.txt")

        # check if user action is "show"

    elif user_action.startswith("show"):

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

        # check if user action is "edit"
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos, "todos.txt")
        except ValueError:
            print("your command is not valid")
            continue

        # check if user action is "complete"
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos, "todos.txt")

            message = f"todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("there is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye!")
