import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# Load the student marks from the JSON file
with open("students.json") as f:
    student_marks = json.load(f)

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist('name')
    marks = [student_marks.get(name) for name in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
