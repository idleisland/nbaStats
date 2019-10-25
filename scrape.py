from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def setUp():
    # NBA season I want to analyze
    year = 2020

    # URL page to scrape
    url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

    # the HTML from the given URL
    html = urlopen(url)

    soup = BeautifulSoup(html)

    # Use findAll() to get the column headers
    soup.findAll('tr', limit=2)

    # Use getText() to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')][1:]

    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

    stats = pd.DataFrame(player_stats, columns = headers).dropna(axis=0)


    for i in range(len(player_stats)):
        if (i not in [20, 41, 62, 83, 104, 125, 146, 167, 188, 209, 230, 251, 272, 293, 314, 335]):
            if (stats['FT%'][i] == ''):
                stats['FT%'][i] = 0
            if (stats['FG%'][i] == ''):
                stats['FG%'][i] = 0
            if (stats['3P%'][i] == ''):
                stats['3P%'][i] = 0
            if (stats['2P%'][i] == ''):
                stats['2P%'][i] = 0
            if (stats['eFG%'][i] == ''):
                stats['eFG%'][i] = 0


    # This makes it so that every single row is displayed but can be commented out
    pd.set_option('display.max_rows', None)

    # This just converts applicable fields from string objects to floats.
    stats[['Age','G','GS','MP','FG','FGA','3P','2P','2PA','FT','FTA','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS','FG%','3P%','2P%','eFG%','FT%']] = stats[['Age','G','GS','MP','FG','FGA','3P','2P','2PA','FT','FTA','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS','FG%','3P%','2P%','eFG%','FT%']].astype('float')
    #print(stats.dtypes)
    print('all set up!')
    return stats

def getPlayerLine(name, stats):
    return stats[stats.Player == name]
    #print(stats.sort_values('eFG%', ascending=False))

def testfunc(blah):
    return blah + 7
