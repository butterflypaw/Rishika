
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"message": "Tasks would be managed locally in this demo."})

if __name__ == '__main__':
    app.run(debug=True)
