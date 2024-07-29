from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {}

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    task_id = task["id"]
    tasks[task_id] = task
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def read_tasks():
    return jsonify(list(tasks.values())), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def read_task(task_id):
    task = tasks.get(task_id)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.json
    if task_id in tasks:
        tasks[task_id].update(updated_task)
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = tasks.pop(task_id, None)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
