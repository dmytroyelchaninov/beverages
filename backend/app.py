from backend import create_app, db
from backend.models import Product, User, Invoice, Tag

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product, 'User': User, 'Invoice': Invoice, 'Tags': Tag}

if __name__ == '__main__':
    app.run()