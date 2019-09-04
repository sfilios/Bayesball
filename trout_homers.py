import info
from ohmysportsfeedspy import MySportsFeeds
from datetime import datetime

msf = MySportsFeeds(version="1.2")
msf.authenticate(info.token, info.pw)

def get_data(date='Today', current_date=True):
    """
    This function is given a date and returns the number of home returns
    hit by Mike Trout on that date (as an integer). Input date should be in YMD
    format as a string i.e. August 9, 2019 is '20190809'. If the current date
    is desired instead of an historical date, let current_date==False.
    Default is to return the number of Homeruns from the current date.
    """

    if current_date==True:
        #get the current date as a string in ymd format
        date = str(datetime.now())
        date = date.replace('-','')
        date = date[:8]
    else:
        pass

    #get the daily player stats from MySportsFeeds API
    daily_data = msf.msf_get_data(league='mlb', season='2019-regular',
    feed='daily_player_stats', fordate=date,
     format='json', player='mike-trout')

    # #get the number of HRs from the JSON file, as a string
    hr_count = daily_data['dailyplayerstats']['playerstatsentry'][0]['stats']['Homeruns']['#text']
    # #convert it into a number
    hr_count = int(hr_count)

    print(daily_data)

    return hr_count

# print(get_data('20190803', current_date=False))
"""
Now that you can get the data for a specific date, you need a way to get it for each game this season.
Get this value for each game, append it to a list. Then you can pass that list into the
mathy stuff.
"""
# Need to generate a list of dates?
