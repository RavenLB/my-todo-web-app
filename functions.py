import json
FILEPATH = "todo.json"

def get_todos(filepath=FILEPATH):
    """ read a text file and return a list of to-do items."""
    with open(filepath, 'r') as file:
        todos_local = json.load(file)  # Load as a list
    return todos_local


def write_todos( todo_arg, filepath=FILEPATH):
    """ write in the list of to-do items."""
    with open(FILEPATH, 'w') as file:
        file.writelines(todo_arg)

def write_json_todos( todo_arg, filepath=FILEPATH):
    """ write in the list of to-do items."""
    with open(FILEPATH, 'w') as file:
        json.dump(todo_arg, file, indent=4)


##if __name__ == "__main__": ##when imported to todo_app.py this won't be executed



def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches":inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters