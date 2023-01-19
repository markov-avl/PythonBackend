import os

from flask import Flask
from flask_bootstrap import Bootstrap5

from controller import *

app = Flask(__name__, template_folder='view', static_folder='static')
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

bootstrap = Bootstrap5(app)


if __name__ == '__main__':
    # app.secret_key = os.urandom(16)
    app.secret_key = b'fs32fsl;f023jisaf[effwoif283rh'
    app.register_blueprint(home_blueprint)
    app.register_blueprint(security_blueprint)
    app.register_blueprint(offer_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(review_blueprint)
    app.register_blueprint(reservations_blueprint)

    app.run(debug=True)
