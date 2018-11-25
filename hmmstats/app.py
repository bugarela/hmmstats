from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import json
import pandas as pd

from hmmstats.resources.media_minuto import MediaMinutoResource
from hmmstats.resources.tops import TopsResource

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

api.add_resource(MediaMinutoResource, '/media_minuto')

api.add_resource(TopsResource, '/tops')

if __name__ == '__main__':
    app.run(debug=True)
