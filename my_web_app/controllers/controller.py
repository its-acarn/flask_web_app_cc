from app import app

@app.route('/')
def index():
    return "Something DEAD cool."

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"