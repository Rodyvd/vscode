from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <h1>Vulnerable Flask App</h1>
        <p>Try the following endpoints to see vulnerabilities in yeah action :</p>
        <ul>
          <li><strong>/greet?name=YourName</strong> - Demonstrates an XSS vulnerability.</li>
          <li><strong>/calc?expr=2+2</strong> - Demonstrates a code injection vulnerability via eval().</li>
        </ul>
    """

@app.route('/greet')
def greet():
    # Vulnerability: Unsanitized user input is directly rendered into HTML.
    name = request.args.get('name', 'Guest')
    # If a user submits something like "<script>alert('XSS');</script>" as the name,
    # it will be rendered and executed by the browser.
    template = f"<h1>Hello, {name}!</h1>"
    return render_template_string(template)

@app.route('/calc')
def calc():
    # Vulnerability: Using eval() on unsanitized input allows execution of arbitrary code.
    expr = request.args.get('expr', '0')
    try:
        result = eval(expr)
    except Exception as e:
        result = f"Error: {e}"
    return f"Result: {result}"

if __name__ == '__main__':
    # Run the app on all network interfaces on port 5000.
    app.run(host='0.0.0.0', port=5000, debug=True)
