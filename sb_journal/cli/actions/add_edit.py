from sb_journal.db import crud
from sb_journal.db.crud.validators import validator_exists, validator_nexists


def _base(method, validator):
    name = input("Enter team name: ")

    try:
        validator(name)
    except Exception as e:
        print("Error:", e)
        return

    seasons = _get_seasons()

    try:
        getattr(crud, method)(name=name, seasons=seasons)
    except Exception as e:
        print("Error:", e)


def _get_seasons():
    while True:
        seasons = input("Enter seasons (space-separated): ")

        try:
            seasons = [int(season) for season in seasons.split()]
        except ValueError:
            print("Invalid seasons entered. Try again.")
            continue

        if not seasons:
            continue

        return seasons


def add():
    return _base("add", validator_nexists)


def edit():
    return _base("edit", validator_exists)
