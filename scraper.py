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
import csv
import os
import pandas as pd
import sqlite3
from tqdm import tqdm

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

# Year loop
for year in tqdm(range(2008,2017), desc = 'Years'):
    # Team loop
    for team in teams:
        # Home/Away loop
        for home_away in loc:
            # Outs loop
            for outs in range(0,3):
                # Inning loop
                for inning in range(1,11):
                    # SQL to check if the data is duplicate
                    if home_away == 'Home':
                        sql = """select game_pk from statcast 
                            where game_year = %s and
                            inning = %s and 
                            outs_when_up = %s and
                            home_team = '%s'
                            """ % (year, inning, outs, team)
                    else:
                        sql = """select game_pk from statcast 
                        where game_year = %s and
                        inning = %s and 
                        outs_when_up = %s and
                        away_team = '%s'
                        """ % (year, inning, outs, team)
                    try:
                        df = pd.read_sql(sql, savant)
                        dup = df.empty
                    except:
                        dup = True
                    if dup == True:
                        # Query link is based on loop input
                        link = 'https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfZ=&hfGT=R%7CPO%7CS%7C&hfPR=&hfAB=&stadium=&hfBBT=&hfBBL=&hfC=&season=' + str(year) + '&player_type=batter&hfOuts=' + str(outs) + '%7C&pitcher_throws=&batter_stands=&start_speed_gt=&start_speed_lt=&perceived_speed_gt=&perceived_speed_lt=&spin_rate_gt=&spin_rate_lt=&exit_velocity_gt=&exit_velocity_lt=&launch_angle_gt=&launch_angle_lt=&distance_gt=&distance_lt=&batted_ball_angle_gt=&batted_ball_angle_lt=&game_date_gt=&game_date_lt=&team=' + team + '&position=&hfRO=&home_road=' + home_away + '&hfInn=' + str(inning) + '%7C&min_pitches=0&min_results=0&group_by=name-event&sort_col=pitches&player_event_sort=start_speed&sort_order=desc&min_abs=0&xba_gt=&xba_lt=&px1=&px2=&pz1=&pz2=&ss_gt=&ss_lt=&is_barrel=&type=details&'
                        # Read in query CSV as dataframe
                        data = pd.read_csv(link)
                        # Rename player_name to denote that it is the batter
                        data.rename(columns={'player_name' : 'batter_name'}, inplace=True)
                        # Append the dataframe to the data
                        pd.io.sql.to_sql(data, name = 'statcast', con = savant, if_exists='append')



