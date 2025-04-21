# Netflix Dataset Cleaning Task

# Dataset Used:
- Original file: `netflix_titles.csv`
- Cleaned file: `cleaned_netflix_titles.csv`

# What Was Done:
This task involved cleaning missing data from the Netflix dataset. Here's what was fixed:
- Replaced all missing values in these text columns with `"Unknown"`:
  - `director`
  - `cast`
  - `country`
  - `date_added`
  - `rating`
- This made the data cleaner and easier to analyze.

# Why "Unknown" Instead of Mean/Median?
- These columns contain **text**, not numbers. So we can't use mean or median.
- Mode could work (most common value), but using `"Unknown"` is more neutral and avoids fake assumptions.

# How to Run the Code:
    python
import pandas as pd

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Fill missing values
cols_to_fill = ['director', 'cast', 'country', 'date_added', 'rating']
df[cols_to_fill] = df[cols_to_fill].fillna('Unknown')

# Save the cleaned dataset
df.to_csv('netflix_titles_cleaned.csv', index=False)
