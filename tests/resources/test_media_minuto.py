import pytest
import json
import pandas as pd

from unittest import TestCase
from hmmstats.app import app


class TestFlaskCase(TestCase):
    def test_media_minuto_post(self):
        cli = app.test_client()

        headers = dict(
            {'Content-Type': 'application/json'}
        )

        data = {'partidas': [1, 2]}

        rv = cli.post('/media_minuto', data=json.dumps(data), headers=headers)
        return_data = json.loads(rv.data)

        self.assertEqual(return_data, {})
