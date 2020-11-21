from flask import Flask, request
from flask_cors import CORS
import sys
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/python',methods=['POST'])
def index():
    data = request.data
    print(data)
    result = subprocess.run([sys.executable, "-c", data], capture_output=True, text=True)
    if result.stdout:
    	return result.stdout
    else:
	    return result.stderr

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
