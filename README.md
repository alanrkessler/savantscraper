# Baseball Savant Data Scraping
Alan Kessler

I would like the acknowledge the valuable contribution of [Joseph Petrich](https://github.com/jpetrich) improving the process and updating for 2017. 

## Background

[Baseball Savant](https://baseballsavant.mlb.com) is a website that contains MLB Statcast data. This data includes data about each pitch such as speed, spin, and location. Most importantly, this source has information about the batted ball such as exit velocity and launch angle. 

The website offers robust querying options. However, for predictive modeling/machine learning purposes, it is useful to have an observation for each pitch. The website currently does not offer this functionality. This project is a result of that need. 

## Table of Contents

- [Data Scraping Notebook](scraper.ipynb)
- [Metadata](metadata.md)

## Disclaimer

Scraping this data takes quite a while. I would suggest breaking up the loop by year or setting aside some time, making sure the machine pulling this data does not fall asleep. 

As always, scraping data from the web may not be welcomed by the source and is important to keep in mind. 
