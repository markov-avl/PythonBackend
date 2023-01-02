from flask import Flask

app = Flask(__name__)

from controllers import index, hello, olimpiads, subject
