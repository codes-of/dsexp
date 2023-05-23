from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/add', methods = ['POST'])
def add():
    data = request.get_json()
    a = data['a']
    b = data['b']

    result = a + b
    answer = jsonify({'result':result})
    return answer

if __name__ == '__main__':
    app.run()
    