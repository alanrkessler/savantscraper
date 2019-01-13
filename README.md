# Baseball Savant Data Scraping
Alan Kessler

## Background

[Baseball Savant](https://baseballsavant.mlb.com) is a website that contains MLB Statcast data. This data includes data about each pitch such as speed, spin, and location. Most importantly, this source has information about the batted ball such as exit velocity and launch angle.

The website offers robust querying options. However, for predictive modeling/machine learning purposes, it is useful to have an observation for each pitch. The website currently does not offer this functionality. The goal of this project is to provide as complete a database of pitches as possible. There are other projects that focus on specific queries or the functions can be easily modified to select different subsets of the data.

------------------
## Resources
-   [Example Query Notebook](examples.ipynb)
-   [Metadata](https://baseballsavant.mlb.com/csv-docs#sv_id)

------------------
## Details

This code pulls data from the Baseball Savant [statcast search tool](https://baseballsavant.mlb.com/statcast_search). It is the equivalent of downloading the detail-level delimited files from the website. The player of interest found in the "player_name" data element refers to the pitcher.

The script loops through teams and seasons to ensure that the queries abide by the search performance limitations. The results can be saved to individual CSV files or loaded into an SQLite database file.

The functions require Python 3.6 or greater.

------------------
## Disclaimer

Scraping this data is time consuming. Scraping data from the web may not be welcomed by its owner.
