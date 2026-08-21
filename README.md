# StarWarsSurvey
This repository contains a Python script for cleaning, analyzing, and visualizing Star Wars survey data. The analysis explores respondent viewership, movie rankings, and breakdowns by gender using `pandas`, `numpy`, and `matplotlib`.

## Features
- **Data Cleaning & Mappings**: Converts text-based responses (Yes/No, movie titles) into boolean and numeric formats for easier aggregation.
- **Viewership Analysis**: Calculates total counts of respondents who have seen each of the first six Star Wars films.
- **Ranking Computations**: Computes average preference rankings for each movie (where lower scores indicate higher preference).
- **Demographic Breakdown**: Splits and compares metrics (viewership and rankings) between male and female respondents.
- **Data Visualizations**: Generates clean bar charts using matplotlib to illustrate rankings and viewership totals overall and by gender.

## Requirements
To run this analysis, ensure you have the following Python libraries installed:
- pandas
- numpy
- matplotlib
You can install the required packages using pip: `pip install pandas numpy matplotlib`

## Dataset
The script expects a dataset named star_wars.csv located in the root directory, encoded with ISO-8859-1.

## Usage
Place the star_wars.csv file in the same directory as your Python script, then run: `python basics.py`
