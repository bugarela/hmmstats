from flask import Flask
from flask_restful import Api

import json
import pandas as pd

from hmmstats.resources.media_minuto import MediaMinutoResource
from hmmstats.resources.tops import TopsResource

app = Flask(__name__)
api = Api(app)

api.add_resource(MediaMinutoResource, '/media_minuto')

api.add_resource(TopsResource, '/tops')

if __name__ == '__main__':
    app.run(debug=True)
