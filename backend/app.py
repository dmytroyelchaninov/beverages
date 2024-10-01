from backend import create_app, db
from backend.models import Product, User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product, 'User': User}

if __name__ == '__main__':
    app.run(debug=True)