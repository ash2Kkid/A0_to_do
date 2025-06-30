from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []

@app.route('/')
def index():
    return "Welcome to Todo API! Use /todos endpoint"

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:index>', methods=['PUT'])
def update_todo(index):
    if index < len(todos):
        todos[index] = request.json
        return jsonify(todos[index])
    return jsonify({"error": "Todo not found"}), 404

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    if index < len(todos):
        deleted = todos.pop(index)
        return jsonify(deleted)
    return jsonify({"error": "Todo not found"}), 404

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
