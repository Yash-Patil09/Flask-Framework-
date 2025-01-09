from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
            symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            symbol = '-'
        elif operation == 'multiply':
            result = num1 * num2
            symbol = '×'
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
                symbol = '÷'
            else:
                return jsonify({"error": "Division by zero is not allowed"})
        else:
            return jsonify({"error": "Invalid operation"})

        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter numeric values."})

if __name__ == '__main__':
    app.run(debug=True)
