from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto permite todas las solicitudes CORS

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.json
    result = data['num1'] + data['num2']
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)
    
    
