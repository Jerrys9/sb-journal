from sb_catalog.db import crud


def view():
    name = input("Enter team name (leave blank to view all): ")
    name = name.strip()

    if not name:
        name = None

    teams = list(crud.get(name))

    if not teams:
        print("No teams to show!")
        return

    for team in teams:
        print(f"\t{team['name']} | Seasons: {team['seasons']}")
