from flask import Flask
from controllers import *

app = Flask(__name__)

if __name__ == '__main__':
    app.secret_key = b'123456789'
    app.register_blueprint(book_blueprint)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(new_reader_blueprint)
    app.register_blueprint(search_blueprint)
    app.register_blueprint(statistics_blueprint)

    app.run()
