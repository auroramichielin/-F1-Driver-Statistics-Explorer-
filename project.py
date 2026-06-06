import csv
import matplotlib.pyplot as plt

def main():

    # Load all CSV files
    drivers = load_drivers()
    results = load_results()
    races = load_races()

    # Ask user for driver name
    research = input("Enter a driver's name to search for: ")

    # Find matching drivers
    matching_drivers = search_driver(research, drivers)
    # No matches found
    if not matching_drivers:
        print("No matching drivers found.")
        return
    # Show matches
    print("\nMatching drivers:")
    # Display matching drivers with numbers
    for i, driver in enumerate(matching_drivers, start=1):
        print(
            f"{i}. {driver['forename']} {driver['surname']} "
            f"(ID: {driver['driverId']})"
        )

    # Select driver 
    selected_driver = input( "\nEnter the number of the driver to view results: ")
    try:
        selected_driver = matching_drivers[int(selected_driver) -1]
    except (ValueError, IndexError):
        print("Invalid selection")
        return

    # Match data (reaults + races)
    driver_results = match_drivers_to_results(results)
    race_names = match_races(races)

    # Display results for every race the driver participated in
    display_driver_results(
        selected_driver,
        driver_results,
        race_names
    )

    # Display total points, wins, wins percentage and average finish position
    points = total_points(selected_driver, driver_results)
    wins = count_wins(selected_driver, driver_results)
    winspercentage = stat_of_wins(selected_driver, driver_results)
    averagefinishposition = average_finish_position(selected_driver, driver_results)
    average_points = average_points_per_race(selected_driver, driver_results)

    print(
        f"\nTotal career points for "
        f"{selected_driver['forename']} "
        f"{selected_driver['surname']}: {points}\n"
        F"{selected_driver['forename']} {selected_driver['surname']} has an average of {average_points:.2f} points per race\n" 
        f"Total wins for {selected_driver['forename']} {selected_driver['surname']}: {wins}\n"
        f"{selected_driver['forename']} {selected_driver['surname']} has won {winspercentage:.2f}% of races he participated in\n"
        f"Average finish position for {selected_driver['forename']} {selected_driver['surname']} during his career: {averagefinishposition:.2f}"
    )

    
    visualization = input("\nWould you like to visualize points over time? (yes/no) ")
    if visualization.lower() == "yes":
        visualize_cumulative_points_over_time(selected_driver, driver_results)


# =========================
# LOAD CSV FILES
# =========================

def load_drivers():
    with open("drivers.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_results():
    with open("results.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_races():
    with open("races.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


# =========================
# SEARCH DRIVER
# =========================

def search_driver(name, drivers):
    matches = []
    for driver in drivers:
        full_name = f"{driver['forename']} {driver['surname']}"
        if name.lower() in full_name.lower():
           matches.append(driver)
    return matches


# =========================
# MATCH RESULTS TO DRIVERS
# =========================

def match_drivers_to_results(results):
    driver_results = {}
    for result in results:
        driver_id = result["driverId"]
        if driver_id not in driver_results:
           driver_results[driver_id] = []
        driver_results[driver_id].append(result)
    return driver_results


# =========================
# MATCH RACE IDs TO NAMES
# =========================

def match_races(races):
    race_names = {}
    for race in races:
       race_names[race["raceId"]] = race["name"]
    return race_names


# =========================
# DISPLAY DRIVER RESULTS
# =========================

def display_driver_results(driver, driver_results, race_names):
    print(
        f"\nResults for "
        f"{driver['forename']} {driver['surname']}:"
    )

    driver_id = driver["driverId"]
    
    if driver_id in driver_results:
        for result in driver_results[driver_id]:
            race_id = result["raceId"]
            race_name = race_names.get(
                race_id,
                "Unknown Race"
            )

            position = result["position"]
            points = result["points"]

            print(
                f"{race_name} | "
                f"Position: {position} | "
                f"Points: {points}"
            )


# =========================
# TOTAL POINTS AND AVERAGE POINTS PER RACE
# =========================

def total_points(driver, driver_results):

    total = 0

    driver_id = driver["driverId"]

    if driver_id in driver_results:
       for result in driver_results[driver_id]:
        total += float(result["points"])

    return total

def average_points_per_race(driver, driver_results):

    driver_id = driver["driverId"]

    if driver_id in driver_results:
        total_points = sum(float(result["points"]) for result in driver_results[driver_id])
        total_races = len(driver_results[driver_id])    
        if total_races > 0:
            average_points = total_points / total_races
        else:
            average_points = 0
   
    return average_points

    
# =========================
# TOTAL WINS
# =========================

def count_wins(driver, driver_results):

    wins = 0

    driver_id = driver["driverId"]

    if driver_id in driver_results:
        for result in driver_results[driver_id]:
            if result["position"] == "1":
                wins += 1

    return wins

# =========================
# STATISTICS (WINS PERCENTAGE)
# =========================

def stat_of_wins(driver, driver_results):

    driver_id = driver["driverId"]

    race_count = len(driver_results.get(driver_id, []))

    wins = count_wins(driver, driver_results)
    if race_count > 0:
        winspercentage = (wins / race_count) * 100
    else:
        winspercentage = 0

    return winspercentage


# =========================
# STATISTICS (AVERAGE FINISH POSITION)
# =========================

def average_finish_position(driver, driver_results):

    driver_id = driver["driverId"]

    positions = [
        int(result["position"])
        for result in driver_results.get(driver_id, [])
        if result["position"].isdigit()
    ]

    if len(positions) > 0:
        averagefinishposition = sum(positions) / len(positions)
    else:
        averagefinishposition = 0

    return round(averagefinishposition, 2)


# =========================
# VISUALIZATION CUMULATIVE POINTS OVER TIME
# =========================

def visualize_cumulative_points_over_time(driver, driver_results):

    driver_id = driver["driverId"]
    # Store race numbers
    races = []
    # Store points
    points = []

    cumulative_points = 0

    if driver_id in driver_results:
        sorted_results = sorted(
            driver_results[driver_id],
            key=lambda result: int(result["raceId"])
        )

        for i, result in enumerate(sorted_results, start=1):

            cumulative_points += float(result["points"])

            races.append(i)
            points.append(cumulative_points)

            
    plt.plot(races, points, marker="o")
    plt.xlabel("Race Number")
    plt.ylabel("Cumulative Points")
    plt.title(
        f"{driver['forename']} "
        f"{driver['surname']} "
        f"Career Points Progression"
    )

    plt.tight_layout()
    plt.show()



# =========================
# RUN PROGRAM
# =========================

if __name__ == "__main__":
    main()