# Baseball Savant Data Scraping
Alan Kessler

## Background

[Baseball Savant](https://baseballsavant.mlb.com) is a website that contains MLB Statcast data. This data includes data about each pitch such as speed, spin, and location. Most importantly, this source has information about the batted ball such as exit velocity and launch angle.

The website offers robust querying options. However, for predictive modeling/machine learning purposes, it is useful to have an observation for each pitch. The website currently does not offer this functionality. The goal of this project is to provide as complete a database of pitch events as possible. There are other projects that focus on specific queries or the functions can be easily modified to select different subsets of the data. This script allows for simple loading of a portable database or the creation of individual files that could be loaded to a storage object like S3 on AWS.

------------------
## Resources
-   [Example Query Notebook](examples.ipynb)
-   [Metadata](https://baseballsavant.mlb.com/csv-docs#sv_id)

------------------
## Details

This code pulls data from the Baseball Savant [statcast search tool](https://baseballsavant.mlb.com/statcast_search). It is the equivalent of downloading the detail-level delimited files from the website. The player of interest found in the "player_name" data element refers to the pitcher.

The script loops through teams, seasons, and home/road to ensure that the queries abide by the search performance limitations. The results can be saved to individual CSV files or loaded into an SQLite database file.

The functions require Python 3.6 or greater.

------------------
## Changes for the 2019 Offseason

-   Split out Home and Road to avoid timeouts more reliably.
-   Removed Deprecated and duplicate columns.
-   Added the ability to change the separator as commas are present in the text-based data elements. The default is now ";". Note that the file is still saved as a ".csv" which means that a program like Excel will not open it correctly. 
-   Changed default sorting to "pitch_number_thisgame" to avoid sorting by launch speed which could be missing. 
-   Prevented returning a dataframe when the CSV is saved. This allows the function to be more flexibly used such as the case of loading the CSVs to AWS.

------------------
## Disclaimer

Scraping this data is time consuming. Scraping data from the web may not be welcomed by its owner.
