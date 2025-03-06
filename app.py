from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():

    pod_name = os.getenv('MY_POD_NAME', 'Unknown Pod')
    
    return f"Hello, User! You are on pod {pod_name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
