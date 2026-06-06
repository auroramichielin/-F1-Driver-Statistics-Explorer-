# F1-Driver-Statistics-Explorer 🏎️
F1 Driver Statistics Explorer is a command-line Python application that lets you search for any Formula 1 driver and explore their complete career statistics — from race-by-race results to total points, win rates, and an interactive points progression chart.
The project is built on real F1 historical data stored in CSV files, and leverages Python's standard library alongside matplotlib for data visualization.

🚀 Features
- 🔍 Driver search — search by first name, last name, or partial name
- 📋 Race-by-race results — view position and points earned for every race in a driver's career
- 📊 Career statistics, including:
     Total career points
     Average points per race
     Total wins
     Win percentage
     Average finish position
- 📈 Cumulative points chart — visualize a driver's points progression over their entire career using matplotlib

⚙️ Requirements
- Python 3.10+
- matplotlib

▶️ How to Run
You'll be prompted to:
- Enter a driver name (or partial name) to search
- Select the correct driver from the matched results
- View that driver's full race history and career stats
- Optionally generate a cumulative points chart

🗃️ Data Sources
The CSV files used in this project are based on the Ergast F1 Dataset, a widely used open dataset covering Formula 1 results from 1950 to the present. https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020/data

🧠 Design Decisions
- CSV over a database: Keeping data in flat CSV files makes the project easy to set up and fully self-contained — no database server required.
- Dictionary-based indexing: Results and races are pre-processed into dictionaries keyed by ID, making lookups efficient rather than scanning lists repeatedly.
- Position filtering: Only numeric finish positions are counted toward average finish position, correctly excluding DNFs, DSQs, and other non-numeric results.
- Cumulative chart sorted by raceId: Races are sorted by raceId (which increases chronologically) to ensure the points progression is displayed in the correct order across a driver's career.

👤 Author
Created as the final project for Harvard's CS50P – Introduction to Programming with Python.
