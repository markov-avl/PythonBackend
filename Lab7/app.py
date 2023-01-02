from flask import Flask

app = Flask(__name__)

app.secret_key = b'123456789'

import controllers.index
import controllers.new_reader
import controllers.book
import controllers.search
import controllers.statistics
