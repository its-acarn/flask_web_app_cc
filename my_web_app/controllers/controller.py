from app import app

@app.route('/')
def index():
    return "Something DEAD cool"

@app.route('/<name>') # ADDED
def greet(name): # ADDED
    return f"Hello {name}!"  # ADDED