import pandas as pd

STATS = ['dano', 'reparo', 'kills', 'deaths', 'assists']


def get_all(partidas):
    df = pd.DataFrame()
    for i in partidas:
        dfi = pd.read_json('partida{}.json'.format(i))
        df = df.append(dfi, ignore_index=True)
    return df


def get_players(df):
    players = pd.DataFrame()

    for nome_time in ['time azul', 'time vermelho']:
        time = pd.DataFrame.from_records(df[nome_time].to_dict()).T
        time['tempo'] = df['tempo de partida']
        time.index = time.nome
        players = players.append(time)

    for stat in STATS:
        players[stat] = players[stat].astype('int')

    players['tempo'] = pd.to_timedelta(
        '00:'+players['tempo']).dt.total_seconds()

    players['bomba'] = pd.to_timedelta(
        '00:'+players['bomba']).dt.total_seconds()

    return players
