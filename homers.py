import info
from ohmysportsfeedspy import MySportsFeeds
from datetime import datetime
from pandas.io.json import json_normalize

msf = MySportsFeeds(version="1.2")
msf.authenticate(info.token, info.pw)

def get_data(player='mike-trout'):
    """
    When called, this function returns a list of the game by game
    homeruns to-date hit by Mike Trout for the 2019 season.
    or you can pass a player of your choice.
    """

    #get the gamelog stats from MySportsFeeds API
    output = msf.msf_get_data(league='mlb', season='2019-regular',
    feed='player_gamelogs', format='json', player=player,
    date='since-20190320')

    #get the number of HRs from the JSON file
    normies = output['playergamelogs']['gamelogs']
    df = json_normalize(normies)

    #it's saved as a string in the dataframe so we change it to an integer
    observed = [int(x) for x in df['stats.Homeruns.#text']]

    return observed

# print(get_data('20190803', current_date=False))
