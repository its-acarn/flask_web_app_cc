from app import app

@app.route('/')
def blablabla():
    return "Something DEAD cool."

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"

@app.route('/hello/james')
def any_function_name():
    return "Hello James!"