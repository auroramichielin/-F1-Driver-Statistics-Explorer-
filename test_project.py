import pytest 
from project import (
    search_driver,
    match_drivers_to_results,
    match_races,
    total_points,
    count_wins,
    stat_of_wins,
    average_finish_position,
    average_points_per_race
)

# =========================
# SAMPLE DATA (used for testing)
# =========================

drivers = [
    {"driverId": "1", "forename": "Lewis", "surname": "Hamilton"},
    {"driverId": "2", "forename": "Max", "surname": "Verstappen"},
]

results = [
    {"driverId": "1", "raceId": "101", "points": "25", "position": "1"},
    {"driverId": "1", "raceId": "102", "points": "18", "position": "2"},
    {"driverId": "2", "raceId": "101", "points": "0", "position": "10"},
]

races = [
    {"raceId": "101", "name": "Monaco GP"},
    {"raceId": "102", "name": "Silverstone GP"},
]

driver_results = match_drivers_to_results(results)

# =========================
# TEST search_driver
# =========================

def test_search_driver():
    matches = search_driver("lewis", drivers)
    assert len(matches) == 1
    assert matches[0]["driverId"] == "1"

# =========================
# TEST match_drivers_to_results
# =========================

def test_match_drivers_to_results():
    assert "1" in driver_results
    assert len(driver_results["1"]) == 2

# =========================
# TEST match_races
# =========================

def test_match_races():
    race_names = match_races(races)
    assert race_names["101"] == "Monaco GP"

# =========================
# TEST total_points
# =========================

def test_total_points():
    driver = drivers[0]
    assert total_points(driver, driver_results) == 43

# =========================
# TEST count_wins
# =========================

def test_count_wins():
    driver = drivers[0]
    assert count_wins(driver, driver_results) == 1

# =========================
# TEST stat_of_wins
# =========================

def test_stat_of_wins():
    driver = drivers[0]
    # 1 win out of 2 races = 50%
    assert stat_of_wins(driver, driver_results) == 50

# =========================
# TEST average_finish_position
# =========================

def test_average_finish_position():
    driver = drivers[0]
    assert average_finish_position(driver, driver_results) == 1.5

# =========================
# TEST average_points_per_race
# =========================

def test_average_points_per_race():
    driver = drivers[0]
    assert round(average_points_per_race(driver, driver_results), 2) == 21.5