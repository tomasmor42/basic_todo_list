from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

from service import get_task, get_all_tasks, create_task


class APIException(Exception):
    status_code = 404

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/tasks")
def tasks_list():
    tasks = get_all_tasks()
    return jsonify(tasks=tasks)

@app.route("/tasks/<int:task_id>")
def task_by_id(task_id):
    task = get_task(task_id)
    if not task:
        raise APIException("Task doesn't exist")
    return jsonify(task=task)

@app.route("/tasks/post", methods=['POST'])
def task_post():
    text = request.args.get('text')
    date = request.args.get('date')
    task_id = create_task(date, text)
    if task_id:
        return jsonify({'task_id':task_id})
    raise APIException(status_code=412, message='Date should be in the future')
    


if __name__ == '__main__':
    app.run()
