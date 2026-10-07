from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/employees/<employee_id>")
def employee(employee_id):
    return jsonify({
        "employeeId": employee_id,
        "department": "Human Resources",
        "status": "ACTIVE"
    })


@app.route("/reports/headcount")
def headcount():
    return jsonify({
        "department": "Human Resources",
        "headcount": 245
    })


if __name__ == "__main__":
    app.run(port=5000)
