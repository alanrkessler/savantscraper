## Baseball Savant Data Scraping

#### Metadata

This metadata is collected from a variety of sources, in some cases verbatim. See References.  

Significant changes were made in 2017 including removing pitch_id. This [article](http://www.hardballtimes.com/research-notebook-new-format-for-statcast-data-export-at-baseball-savant/) in the Hardball Times for details.

- `pitch_type` - type of pitch based on a neural network classification:
	- `CH` Changeup
	- `CU` Curveball
	- `EP` Eephus
	- `FA` Fastball
	- `FC` Cutter
	- `FF` Four seam Fastball
	- `FS` Splitter
	- `FT` Two seam Fastball
	- `FO` Forkball
	- `IN` Intent ball
	- `KC` Knuckle ball Curve
	- `KN` Knuckle ball
	- `PO` Pitch Out
	- `SC` Screwball
	- `SI` Sinker
	- `SL` Slider
- `game_date`	- date game was played
- `release_speed` - pitch speed in miles per hour, measured at the initial point, y0. The field y0 has changed at times but is not available on this source. (renamed start_speed; note that it is now measured by StatCast, not PITCHf/x
- `release_pos_x` - horizontal position of the pitch at y0 (renamed x0)
- `release_pos_z` - vertical position of the pitch at y0 (renamed z0)
- `batter_name` - name of batter
- `batter` - MLB ID of batter	
- `pitcher` - MLB ID of pitcher	
- `events` - 	at bat event:
	- Bunt Groundout
	- Bunt Lineout
	- Bunt Pop Out
	- Double
	- Double Play
	- Field Error
	- Fielders Choice
	- Fielders Choice Out 
	- Flyout
	- Forceout
	- Grounded into DP
	- Groundout
	- Hit By Pitch
	- Home Run
	- Intent Walk
	- Lineout
	- Pop Out
	- Runner Out
	- Sac Bunt
	- Sac Fly
	- Sac Fly DP
	- Single
	- Strikeout
	- Strikeout - DP
	- Triple
	- Walk
- `description` - description of result of the specific pitch:
	- Automatic Ball
	- Ball
	- Ball In Dirt
	- Called Strike
	- Foul
	- Foul (Runner Going)
	- Foul Bunt
	- Foul Tip
	- Hit By Pitch
	- In play, no out
	- In play, out(s)
	- In play, run(s)
	- Intent Ball
	- Missed Bunt
	- Pitchout
	- Swinging Strike
	- Swinging Strike (Blocked)
- `spin_dir` - direction of spin in degrees
- `spin_rate_deprecated` - ball spin in revolutions per minute (renamed spin_rate)
- `break_angle_deprecated` - the angle, in degrees, from vertical to the straight line path from the release point to where the pitch crossed the front of home plate, as seen from the catcher’s/umpire’s perspective (renamed break_angle)
- `break_length_deprecated` - the measurement of the greatest distance, in inches, between the trajectory of the pitch at any point between the release point and the front of home plate, and the straight line path from the release point and the front of home plate (renamed break_length)
- `zone` - mapping of where ball crosses the plate from the pitcher's perspective. The zone is divided up into a 3x3 grid. Zone 1 is high and inside to a left handed hitter, Zone 4 middle and inside, and Zone 9 would be low and outside. Zones 11, 12, 13, and 14 represent areas outside of the strike zone and follow the same left to right counting scheme.  
- `des` - play-by-play description of the result of the at bat
- `game_type` - type of game: `S` spring training, `R` regular season, `P` playoffs	
- `stand` - handedness of batter's stance: `L` left or `R` right	
- `p_throws` - handedness of pitcher: `L` left or `R` right
- `home_team` - team abbreviation of the home team 
- `away_team` - team abbreviation of the away team
- `type` - result type: `B` ball, `S` strike, or `X` in play
- `hit_location` - numerical position ball was hit to (e.g. `6` would suggest short stop). Shows `0` if not applicable (e.g. a walk).	
- `bb_type` - batted ball type
	- `0`: unknown
	- `1`: flyball
	- `2`: popup
	- `3`: line drive
	- `4`: ground ball
- `balls` - number of balls for the batter before the pitch was thrown	
- `strikes`- number of strikes on the batter before the picth was thrown
- `game_year` - year of game date	
- `pfx_x` - the horizontal movement, in inches, of the pitch between the release point and home plate, as compared to a theoretical pitch thrown at the same speed with no spin-induced movement. This parameter is measured at y=40 feet regardless of the y0 value.	
- `pfx_z` - the vertical movement, in inches, of the pitch between the release point and home plate, as compared to a theoretical pitch thrown at the same speed with no spin-induced movement. This parameter is measured at y=40 feet regardless of the y0 value.	
- `plate_x` - the left/right distance, in feet, of the pitch from the middle of the plate as it crossed home plate. The PITCHf/x coordinate system is oriented to the catcher’s/umpire’s perspective, with distances to the right being positive and to the left being negative. (renamed px)
- `plate_z` - the height of the pitch in feet as it crossed the front of home plate. (renamed pz)	
- `on_3b` - MLB ID of runner on third base. Null if no runner.
- `on_2b` - MLB ID of runner on second base. Null if no runner.
- `on_1b` - MLB ID of runner on first base. Null if no runner.
- `outs_when_up` - outs when the batter was up
- `inning` - inning the batter was up	
- `inning_topbot` - half inning indicator: `top` top or `bot` bottom
- `hc_x` - horizontal location of batted ball (0 to 250). Bottom left corner of top down view of baseball field is (0, -250). Top right is (250, 0).
- `hc_y` - shallow/deep location of batted ball (-250 to 0). Bottom left corner of top down view of baseball field is (0, -250). Top right is (250, 0).
- `tfs_deprecated` - UTC time (renamed tfs)
- `tfs_zulu_deprecated` - UTC timestamp	(renamed tfs_zulu)
- `pos2_person_id` - MLB ID of catcher (renamed catcher)
- `umpire` - MLB ID of umpire	
- `sv_id` - a date/time stamp of when the PITCHf/x tracking system first detected the pitch in the air, it is in the format YYMMDD_hhmmss	http://m.mlb.com/glossary/statcast
- `vx0` - initial horizontal velociy of pitch in feet per second	
- `vy0` - initial velocity of pitch in direction of batter in feet per second 	
- `vz0` - initial vertical velocity of pitch in feet per second
- `ax` - initial horizontal acceleration of pitch in feet per second per second per second	
- `ay` - initial acceleration of pitch in direction of batter in feet per second per second per second
- `az`- initial vertical acceleration of pitch in feet per second per second per second	
- `sz_top` - the distance in feet from the ground to the top of the current batter’s rulebook strike zone as measured from the video by the PITCHf/x operator. The operator sets a line at the batter’s belt as he settles into the hitting position, and the PITCHf/x software adds four inches up for the top of the zone.
- `sz_bot` - the distance in feet from the ground to the bottom of the current batter’s rulebook strike zone. The PITCHf/x operator sets a line at the hollow of the knee for the bottom of the zone.	
- `hit_distance_sc` - hit distance in feet
- `launch_speed` - exit velocity in mph	(renamed hit_speed)
- `launch_angle` - angle of ball hit in degrees (renamed hit_angle)
- `effective_speed` - perceived velocity of pitch in mph
- `release_spin_rate` - rate of spin after ball is released
- `release_extension` - how much closer, in feet, the pitch is released compared to the rubber. 
- `game_pk` - related to the Game Day package
- `pos1_person_id` - pitcher's MLB ID
- `pos2_person_id.1` - catcher's MLB ID
- `pos3_person_id` - first baseman's MLB ID
- `pos4_person_id` - second basemen's MLB ID
- `pos5_person_id` - third baseman's MLB ID
- `pos6_person_id` - shortstop's MLB ID
- `pos7_person_id` - left fielder's MLB ID
- `pos8_person_id` - center fielder's MLB ID
- `pos9_person_id` - right fielder's MLB ID
- `estimated_ba_using_speedangle` - average BA on balls with a similar exit velocity and launch angle
- `estimated_woba_using_speedangle` - average wOBA on balls with a similar exit velocity and launch angle
- `woba_value` - wOBA numerator
- `woba_denom` - wOBA denominator
- `babip_value` - batting average ball on balls in play for the single event
- `iso_value` - isolated power for the single event

#### References 

[Mike Fast's PITCHf/x glossary](https://fastballs.wordpress.com/category/pitchfx-glossary/)

[/r/Sabermetrics user rjweise](https://docs.google.com/document/d/1ztD20pt5K0HUi2EcJHT4SYdOZw9YPYhtLUmi8BpInuA/edit?pref=2&pli=1#heading=h.gjdgxs)

[MLB Glossary - Statcast](http://m.mlb.com/glossary/statcast)

[The Hardball Times - Research Notebook: New Format for Statcast Data Export at Baseball Savant](http://www.hardballtimes.com/research-notebook-new-format-for-statcast-data-export-at-baseball-savant/)
