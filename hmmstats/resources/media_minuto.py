from flask import Flask, request
from flask_restful import Resource, Api

import pandas as pd

from hmmstats.data import get_all, get_players, STATS


class hmmstatsResource(Resource):
    def json(self):
        return request.get_json()


class MediaMinutoResource(hmmstatsResource):
    def post(self):
        input = self.json()

        df = get_all(input['partidas'])
        players = get_players(df)

        return_data = pd.DataFrame()

        for stat in STATS:
            return_data[stat] = 60 * players[stat] / players['tempo']

        return_data['bomba'] = players['bomba'] / players['tempo']

        return return_data.to_dict()
