from flask import Flask
from controllers import *

app = Flask(__name__, template_folder='templates', static_folder='static')

if __name__ == '__main__':
    app.register_blueprint(index_blueprint)
    app.register_blueprint(hello_blueprint)
    app.register_blueprint(olimpiads_blueprint)
    app.register_blueprint(subject_bluprint)

    app.run()
