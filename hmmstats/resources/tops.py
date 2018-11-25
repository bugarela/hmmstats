from flask import Flask, request
from flask_restful import Resource, Api

import pandas as pd

from hmmstats.data import get_all, get_players, STATS


class hmmstatsResource(Resource):
    def json(self):
        return request.get_json()


class TopsResource(hmmstatsResource):
    def post(self):
        input = self.json()

        df = get_all(input['partidas'])
        players = get_players(df)

        stat = input['stat']
        minuto = input['minuto']

        if(minuto):
            players[stat] = 60 * players[stat] / players['tempo']

        top_val = players[stat].max()
        return_data = players[players[stat] == top_val]

        return return_data.to_dict()
