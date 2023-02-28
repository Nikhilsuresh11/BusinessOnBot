from flask import Flask, request, jsonify
from rasa_nlu.model import Interpreter

app = Flask(__name__)

interpreter = Interpreter.load("<path-to-your-model>")


@app.route('/webhooks/your_flask_endpoint', methods=['POST'])
def respond():
    user_message = request.json['message']
    response = interpreter.parse(user_message)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
