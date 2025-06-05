
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "charts": [{"id": 1, "value": "Chart Data"}],
        "tables": [{"id": 1, "value": "Table Data"}],
        "notifications": [{"id": 1, "message": "Notification 1"}]
    })

if __name__ == '__main__':
    app.run(debug=True)
