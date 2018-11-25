from flask import Flask, request
from flask_restful import Resource, Api

import pandas as pd

from hmmstats.data import get_all, get_players, STATS, TIME_STATS


class hmmstatsResource(Resource):
    def json(self):
        return request.get_json()


class TopsResource(hmmstatsResource):
    def post(self):
        input = self.json()

        df = get_all(input['partidas'])
        players = get_players(df)

        minuto = input['minuto']

        return_data = dict()

        for stat in STATS:
            if(minuto):
                players[stat] = 60 * players[stat] / players['tempo']

            top_val = players[stat].max()
            return_data[stat] = players[players[stat]
                                        == top_val].to_dict('records')

        for time_stat in TIME_STATS:
            if(minuto):
                players[time_stat] = 60 * players[time_stat] / players['tempo']

            top_val = players[time_stat].max()
            return_data[time_stat] = players[players[time_stat]
                                             == top_val].to_dict('records')

        return return_data
