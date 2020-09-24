from app import app

@app.route('/')
def blablabla():
    return "Something DEAD cool."

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"

@app.route('/h/a')
def yp():
    return "Hello james!"