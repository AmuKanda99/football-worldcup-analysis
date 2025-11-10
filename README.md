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

### The rationale to map the business requirements to the Data Visualisations

- Average goal per team over the different World Cup tournaments.
- Points distribution of teams over the different World Cup tournaments.
- Collective points distribution over the different World Cup tournaments.
- Top 4 retention rate
- Goal difference vs Points
- Defense vs Offense importance
- Point distribution by draw count

### Analysis techniques used

- Used generative AI tools (Github Copilot, ChatGPT and Claude) for code suggestions, design thinking and correction
- Matplotlib, Seaborn and Plotly plots used to visualise data
- Descriptive analysis used to summarise and explain data

### Ethical considerations

- Ensure the dataset was publicly available or properly licensed.
- Be cautious not to frame smaller or lower-ranked teams as “less entertaining” purely due to lower performance metrics.
- Recognize that entertainment value is subjective and may reflect cultural or regional biases.
- Clearly communicate that statistical patterns indicate correlation, not causation.
- Consider that maximizing “entertainment” should not come at the cost of player well-being, match fairness, or accessibility for fans.

### Dashboard Design

Home page includes dataset and visualisations

### Unfixed Bugs

No significant unfixed bug

### Development Roadmap

- Data was separated in different CSV files, these files were put together in order to work efficiently
- Data types were changed to have a clear visualisation
- Future improvements include working on a better dashboard result

### Main Data Analysis libraries

- pandas
- numpy
- plotly
- streamlit

## Credits

#### Content

- Kaggle
- Code Institute LMS

### Acknowledgements

Thanks to the Code Institute instructors and peers for feedback and support
