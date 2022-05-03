from sb_catalog.storage import crud
from sb_catalog.storage.crud.validators import validator_nexists


def add():
    name = input("Enter team name: ")
    try:
        validator_nexists(name)
    except ValueError as e:
        print("Error:", e)
        return

    seasons = input("Enter seasons (space-separated): ")
    try:
        seasons = [int(season) for season in seasons.split()]
    except ValueError:
        print("Error: invalid seasons entered.")
        return

    try:
        crud.add(name=name, seasons=seasons)
    except Exception as e:
        print("Error:", e)
