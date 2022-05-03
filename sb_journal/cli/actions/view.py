from sb_journal.db import crud


def view():
    name = input("Enter team name (leave blank to view all): ")

    if not name:
        name = None

    try:
        teams = list(crud.get(name))
    except Exception as e:
        print("Error:", e)
        return

    if not teams:
        print("No teams to show!")
        return

    for team in teams:
        print(
            "\t", team['name'], " | Seasons: ", team['seasons'],
            sep="",
        )
