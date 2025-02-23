from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD !"  # Omission de l'exclamation

@app.route('/status')
def status():
    return "Application is running!"

if __name__ == "__main__":
    app.run(debug=True)
