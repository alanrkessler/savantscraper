from __future__ import print_function
'''
Copyright (C) 2017
Author: Alan Kessler

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

# Baseball Savant Data Scraping

import requests
import os
import pandas as pd
import sqlite3
from tqdm import tqdm
import time
from urllib2 import HTTPError


# Connect to database
savant = sqlite3.connect('BaseballSavant.db')

# List of teams
teams = ['LAA', 'HOU', 'OAK', 'TOR', 'ATL', 'MIL', 'STL', 
         'CHC', 'ARI', 'LAD', 'SF', 'CLE', 'SEA', 'MIA', 
         'NYM', 'WSH', 'BAL', 'SD', 'PHI', 'PIT', 'TEX', 
         'TB', 'BOS', 'CIN', 'COL', 'KC', 'DET', 'MIN', 
         'CWS', 'NYY']

# List of Home/Road
loc = ['Home', 'Road']

# List of out combinations
outl = ['0', '1', '2%7C3']
alreadyPrinted = False
# Year loop
for year in tqdm(range(2008, 2017), desc = 'Years'):
    # Team loop
    for team in tqdm(teams, desc = 'Teams', leave = False):
        # Home/Away loop
        for home_away in tqdm(loc, desc = 'Location', leave = False):
            # Inning loop
            for inning in tqdm(range(1, 11), desc='Innings', leave=False):
                # Outs loop
                for outs in tqdm(outl, desc = 'Outs', leave = False):
                    # pitcher handedness
                    for throws in ['R', 'L']:
                        # Query link is based on loop input
                        link = 'https://baseballsavant.mlb.com/statcast_search/csv?all=true\
                        &hfGT=R%7CPO%7CS%7C&hfPR=\
                        &season=' + str(year) + '&player_type=batter\
                        &hfOuts=' + outs + '%7C&team=' + team + '&position=&hfRO=\
                        &home_road=' + home_away + '&hfInn=' + str(inning) + '%7C&min_pitches=0\
                        &pitcher_throws=' + throws + '&min_results=0&group_by=name&sort_col=pitches\
                        &player_event_sort=start_speed\
                        &sort_order=desc&min_abs=0&xba_gt=&xba_lt=&px1=&px2=&pz1=&pz2=&ss_gt=&ss_lt=&is_barrel=&type=details&'

                        successful = False
                        backoff_time = 30
                        while not successful:
                            try:
                                # Read in query CSV as dataframe
                                raise HTTPError(msg='Test error', url='http://fake.com', code=502, hdrs='', fp=None)
                                data = pd.read_csv(link)
                                # Rename player_name to denote that it is the batter
                                data.rename(columns={'player_name': 'batter_name'}, inplace=True)
                                # Append the dataframe to the data
                                # pd.io.sql.to_sql(data, name='statcast', con=savant, if_exists='append')
                                successful = True
                            except (HTTPError, sqlite3.OperationalError) as e:
                                # If there is an error, sleep and try one more time
                                for i in tqdm(range(1, backoff_time), desc="Backing off " + str(backoff_time) + " seconds for error " + str(e) + " at " + str(year) + " " + outs + " " + team + " " + home_away + " " + str(inning), leave=False):
                                    time.sleep(1)
                                backoff_time = min(backoff_time * 2, 60*60)

# Commit and close connection
savant.commit() 
savant.close()
