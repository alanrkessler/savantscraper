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

# Year loop
for year in tqdm(range(2008, 2017), desc = 'Years'):
    # Team loop
    for team in teams:
        # Home/Away loop
        for home_away in loc:
            # Outs loop
            for outs in outl:
                # Inning loop
                for inning in range(1,11):
                    # Query link is based on loop input
                    link = 'https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfZ=&hfGT=R%7CPO%7CS%7C&hfPR=&hfAB=&stadium=&hfBBT=&hfBBL=&hfC=&season=' + str(year) + '&player_type=batter&hfOuts=' + outs + '%7C&pitcher_throws=&batter_stands=&start_speed_gt=&start_speed_lt=&perceived_speed_gt=&perceived_speed_lt=&spin_rate_gt=&spin_rate_lt=&exit_velocity_gt=&exit_velocity_lt=&launch_angle_gt=&launch_angle_lt=&distance_gt=&distance_lt=&batted_ball_angle_gt=&batted_ball_angle_lt=&game_date_gt=&game_date_lt=&team=' + team + '&position=&hfRO=&home_road=' + home_away + '&hfInn=' + str(inning) + '%7C&min_pitches=0&min_results=0&group_by=name&sort_col=pitches&player_event_sort=start_speed&sort_order=desc&min_abs=0&xba_gt=&xba_lt=&px1=&px2=&pz1=&pz2=&ss_gt=&ss_lt=&is_barrel=&type=details&'
                    try:
                        # Read in query CSV as dataframe
                        data = pd.read_csv(link)
                    except HTTPError:
                        # If there is an error, sleep and try one more time
                        time.sleep(10)
                        # Read in query CSV as dataframe
                        data = pd.read_csv(link)
                    # Rename player_name to denote that it is the batter
                    data.rename(columns={'player_name' : 'batter_name'}, inplace=True)
                    # Append the dataframe to the data
                    pd.io.sql.to_sql(data, name = 'statcast', con = savant, if_exists='append')
                    
# Delete any duplicate pitches
s = savant.cursor()

s.execute('''DELETE FROM statcast WHERE rowid NOT IN (SELECT MIN(rowid) FROM statcast GROUP BY game_pk, pitch_id, game_year, inning, outs_when_up)''')

# Commit and close connection
savant.commit() 
savant.close()