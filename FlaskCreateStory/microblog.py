from routes import *

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

app.run()