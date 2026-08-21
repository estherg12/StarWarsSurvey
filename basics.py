import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the Star Wars survey data
star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")

# Preview the first 10 rows
print(star_wars.head(10))

# Display the column names
print(star_wars.columns)

yes_no = {
    "Yes": True,
    "No": False
}

star_wars["Have you seen any of the 6 films in the Star Wars franchise?"] = (
    star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].map(yes_no)
)

star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"] = (
    star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].map(yes_no)
)

print(
    star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].value_counts(
        dropna=False
    )
)

print(
    star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].value_counts(
        dropna=False
    )
)

# Map each movie-title response to True; treat blank responses as False
movie_mapping = {
    "Star Wars: Episode I  The Phantom Menace": True,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True,
    np.nan: False
}

# Convert the six checkbox-answer columns
for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(movie_mapping)

# Rename the columns
star_wars = star_wars.rename(columns={
    "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
    "Unnamed: 4": "seen_2",
    "Unnamed: 5": "seen_3",
    "Unnamed: 6": "seen_4",
    "Unnamed: 7": "seen_5",
    "Unnamed: 8": "seen_6"
})

print(star_wars.columns[3:9])

print(star_wars[[
    "seen_1", "seen_2", "seen_3",
    "seen_4", "seen_5", "seen_6"
]].head())

# Convert ranking responses to numeric floats
star_wars[star_wars.columns[9:15]] = star_wars[
    star_wars.columns[9:15]
].astype(float)

# Rename ranking columns
star_wars = star_wars.rename(columns={
    "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
    "Unnamed: 10": "ranking_2",
    "Unnamed: 11": "ranking_3",
    "Unnamed: 12": "ranking_4",
    "Unnamed: 13": "ranking_5",
    "Unnamed: 14": "ranking_6"
})

print(star_wars.columns[9:15])
print(star_wars[[
    "ranking_1", "ranking_2", "ranking_3",
    "ranking_4", "ranking_5", "ranking_6"
]].head())

# Calculate the mean rank for every movie
ranking_means = star_wars[
    ["ranking_1", "ranking_2", "ranking_3",
     "ranking_4", "ranking_5", "ranking_6"]
].mean()

# Display the averages
print(ranking_means)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(ranking_means.index, ranking_means.values)

plt.title("Average Star Wars Movie Rankings")
plt.xlabel("Movie")
plt.ylabel("Average ranking (lower is better)")
plt.show()

movie_labels = [
    "Episode I",
    "Episode II",
    "Episode III",
    "Episode IV",
    "Episode V",
    "Episode VI"
]

plt.figure(figsize=(10, 6))
plt.bar(movie_labels, ranking_means.values)

plt.title("Average Star Wars Movie Rankings")
plt.xlabel("Movie")
plt.ylabel("Average ranking (1 = favorite; 6 = least favorite)")
plt.show()

# Count how many respondents saw each movie
seen_counts = star_wars[
    ["seen_1", "seen_2", "seen_3", "seen_4", "seen_5", "seen_6"]
].sum()

# Display the counts
print(seen_counts)

# Create a bar chart
movie_labels = [
    "Episode I",
    "Episode II",
    "Episode III",
    "Episode IV",
    "Episode V",
    "Episode VI"
]

plt.figure(figsize=(10, 6))
plt.bar(movie_labels, seen_counts.values)

plt.title("Number of Respondents Who Saw Each Star Wars Movie")
plt.xlabel("Movie")
plt.ylabel("Number of respondents who saw the movie")
plt.show()

# Split the dataframe by gender
males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]

ranking_columns = [
    "ranking_1", "ranking_2", "ranking_3",
    "ranking_4", "ranking_5", "ranking_6"
]

# Find mean ranking by gender
male_ranking_means = males[ranking_columns].mean()
female_ranking_means = females[ranking_columns].mean()

print("Male average rankings:")
print(male_ranking_means)

print("\nFemale average rankings:")
print(female_ranking_means)

movie_labels = [
    "Episode I", "Episode II", "Episode III",
    "Episode IV", "Episode V", "Episode VI"
]

plt.figure(figsize=(10, 6))
plt.bar(movie_labels, male_ranking_means.values)
plt.title("Average Star Wars Rankings: Male Respondents")
plt.xlabel("Movie")
plt.ylabel("Average ranking (lower is better)")
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(movie_labels, female_ranking_means.values)
plt.title("Average Star Wars Rankings: Female Respondents")
plt.xlabel("Movie")
plt.ylabel("Average ranking (lower is better)")
plt.show()

seen_columns = ["seen_1", "seen_2", "seen_3", "seen_4", "seen_5", "seen_6"]

# Count viewers by gender
male_seen_counts = males[seen_columns].sum()
female_seen_counts = females[seen_columns].sum()

print("Male viewership totals:")
print(male_seen_counts)

print("\nFemale viewership totals:")
print(female_seen_counts)

plt.figure(figsize=(10, 6))
plt.bar(movie_labels, male_seen_counts.values)
plt.title("Star Wars Movie Viewership: Male Respondents")
plt.xlabel("Movie")
plt.ylabel("Number of respondents who saw the movie")
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(movie_labels, female_seen_counts.values)
plt.title("Star Wars Movie Viewership: Female Respondents")
plt.xlabel("Movie")
plt.ylabel("Number of respondents who saw the movie")
plt.show()

x = np.arange(len(movie_labels))
width = 0.4

plt.figure(figsize=(11, 6))
plt.bar(x - width / 2, male_ranking_means.values, width, label="Male")
plt.bar(x + width / 2, female_ranking_means.values, width, label="Female")

plt.xticks(x, movie_labels)
plt.title("Average Star Wars Rankings by Gender")
plt.xlabel("Movie")
plt.ylabel("Average ranking (lower is better)")
plt.legend()
plt.show()