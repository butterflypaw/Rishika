
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = [
        {"Name": "Alice", "Age": 25, "Location": "New York"},
        {"Name": "Bob", "Age": 30, "Location": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "Location": "Chicago"},
        {"Name": "Diana", "Age": 40, "Location": "Houston"},
        {"Name": "Eve", "Age": 45, "Location": "Phoenix"},
    ] * 20  # Mock large dataset
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
