from sb_journal.db.client import get_db_collection


def show_prompt(actions):
    db_collection = get_db_collection()
    count = db_collection.count_documents({})

    print("There are", count, "teams in the DB.")
    print()

    print("Actions:")
    for _, name, description in actions:
        print(
            "\t(", name[0], ")", name[1:], " \u2014 ", description,
            sep="",
        )
