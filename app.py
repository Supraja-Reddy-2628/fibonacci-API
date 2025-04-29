from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci number cannot be computed for negative numbers.")

    first = 0
    second = 1
    count = 0

    while count < n:
        next_number = first + second
        first = second
        second = next_number
        count += 1

    return first

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    try:
        # Fetch 'n' parameter from the query string
        number_param = request.args.get('n')

        if number_param is None:
            return jsonify({
                'status': 400,
                'message': 'Parameter "n" is required and must be an integer',
                'error': 'Missing query parameter'
            }), 400

        try:
            number = int(number_param)  # Ensure 'n' is an integer
        except ValueError:
            return jsonify({
                'status': 400,
                'message': 'The "n" parameter must be an integer',
                'error': 'Invalid data type'
            }), 400

        result = fibonacci(number)
        return jsonify({
            'status': 200,
            'message': 'Fibonacci successfully calculated',
            'number': number,
            'fibonacci': result
        }), 200

    except ValueError as ve:
        return jsonify({
            'status': 400,
            'message': 'Invalid input: Fibonacci number cannot be computed for negative numbers',
            'error': str(ve)
        }), 400

    except Exception as e:
        return jsonify({
            'status': 500,
            'message': 'An unexpected error occurred',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
