import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

# Load the student marks from the JSON file
with open("q-vercel-python.json") as f:
    students_data = json.load(f)

# Create a dictionary mapping names to marks
student_marks = {student["name"]: student["marks"] for student in students_data}

@app.route("/api", methods=["GET"])
def get_marks():
    # Get the names from the query parameters
    names = request.args.getlist('name')
    # Fetch the marks for the given names
    marks = [student_marks.get(name, None) for name in names]  # Use None if name not found
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
