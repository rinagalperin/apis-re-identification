from flask import Flask, jsonify, request

app = Flask(__name__)

mock_employees = {
    1: {'salary': 50000, 'role': 'Developer', 'age': 30, 'department': 'IT'},
    2: {'salary': 60000, 'role': 'Manager', 'age': 35, 'department': 'HR'},
    3: {'salary': 70000, 'role': 'Developer', 'age': 28, 'department': 'IT'},
    4: {'salary': 80000, 'role': 'Analyst', 'age': 32, 'department': 'Finance'},
    5: {'salary': 90000, 'role': 'Manager', 'age': 40, 'department': 'HR'}
}


def fetch_total_payroll():
    total_salary = sum(employee['salary'] for employee in mock_employees.values())
    return total_salary


def fetch_filtered_payroll(role=None, age=None, department=None):
    filtered = sum(employee['salary']
                   for employee in mock_employees.values()
                   if (role is None or str(employee['role']).lower() == str(role).lower())
                   and (age is None or str(employee['age']).lower() == str(age).lower())
                   and (department is None or str(employee['department']).lower() == str(department).lower())
                   )
    return fetch_total_payroll()-filtered


@app.route('/api/total_payroll', methods=['GET'])
def get_total_payroll():
    total_salary = fetch_total_payroll()
    return jsonify({'total_salary': total_salary})


@app.route('/api/total_payroll/exclude_criteria', methods=['GET'])
def get_filtered_payroll():
    role = request.args.get('role')
    age = request.args.get('age')
    department = request.args.get('department')

    total_salary_excluding = fetch_filtered_payroll(role, age, department)
    return jsonify({'total_salary_excluding': total_salary_excluding})


if __name__ == '__main__':
    app.run(debug=True)

    # Example usage:
    # Step 1: request the sum of salaries for all employees:
    # curl http://localhost:5000/api/total_payroll

    # Step 2: request the sum of salaries again, but this time excluding the target:
    # curl 'http://localhost:5000/api/total_payroll/exclude_criteria?age=35&department=HR'

    # Step 3: subtract the two sums to isolate the target's salary
