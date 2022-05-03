from sb_journal.db import crud


def delete():
    name = input("Enter team name (leave blank to delete all): ")

    if not name:
        name = None

    try:
        crud.delete(name)
    except Exception as e:
        print("Error:", e)
