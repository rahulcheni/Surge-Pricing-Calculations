from flask import Flask
app = Flask(__name__)

import logging
log = logging.getLogger('test')
log.setLevel(logging.ERROR)

from app import insight
