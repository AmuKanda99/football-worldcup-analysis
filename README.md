# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## FIFA - Football World Cup entertainment analysis

This project analyses historical FIFA World Cup data to explore how future tournaments can be designed to maximize entertainment. It features a reproducible data pipeline for collection, cleaning, and feature engineering across match and event-level data. The analysis applies statistical modeling and exploratory analytics to uncover drivers of excitement — including scoring patterns and competitive balance.

### Dataset Content

The dataset includes key features such as team names, final placements, goals for and against, wins, and total points. The dataset was gathered from Kaggle.

### Business Requirements

- Give an understanding of how points, wins, draws and losses affect the competitiveness of a team
- Provide insights to how a strong defense and a strong attack compare to each other
- Be able to show if there is correlation between placing well in a World Cup and if that affacts the placing in the following one

### Hypothesis and how to validate?

- Hypothesis 1: The average number of goals per team per World Cup has increased over time.
- Hypothesis 2: The distribution of points per team has become more balanced over time.
- Hypothesis 3: Teams that performed well in one World Cup (top 4) tend to perform well in the next.
- Hypothesis 4: Teams with higher goal differences (goals for - goals against) achieve more points.
- Hypothesis 5: A strong defense (fewer goals_against) contributes more to success than a strong offense (goals for).
- Hypothesis 6: Teams that draw fewer matches tend to earn more total points.

### Project Plan

- Data collection from Kaggle.
- Data unified into a single dataset.
- Data cleaning and preprocessing in Jupyter notebooks.
- Exploratory analysis and feature engineering.
- Machine Learning .
- Dashboard development in Streamlit.
- Iterative testing and refinement based on feedback.
