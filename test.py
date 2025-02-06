from flask import Flask

secret_key = 'yeah' 

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = secret_key  # Noncompliant

@app.route('/')
def home():
    return "Hello, Flask!"


if __name__ == '__main__':
    app.run(debug=True)