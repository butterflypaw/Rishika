
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/data")
def get_data():
    return jsonify({
        "chart": [1, 2, 3],
        "table": [{"name": "Item 1"}, {"name": "Item 2"}],
        "notifications": ["New message", "Server rebooted"]
    })

if __name__ == "__main__":
    app.run(debug=True)
