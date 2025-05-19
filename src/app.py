from flask import Flask, jsonify, request

app = Flask(__name__)


# dummy data
todos = [
    { "label": "My first task", "done": False, "id": 1 },
    { "label": "My second task", "done": False, "id": 2 },
]


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200


@app.route('/todos', methods=['POST'])
def add_todo():
    request_body = request.json
    print('Received new request!', request_body)
    todos.append(request_body)

    response = {
        'message': 'Received response from POST method',
        'data': todos
    }
    return jsonify(response), 200


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Deleting todo: ", position)
    for todo in todos:
        if todo.get('id') == position:
            todos.remove(todo)
            break
    
    response = {
        'message': 'Received response from DELETE method',
        'data': todos
    }
    return jsonify(response), 200





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)