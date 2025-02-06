from flask import Flask

# Define your secret key
secret_key = 'your_secret_key_here'  # Replace with your actual secret key

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = secret_key  # Noncompliant

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)