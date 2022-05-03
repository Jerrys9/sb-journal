from sb_catalog.db.client import get_db_collection


def show_prompt(actions):
    db_collection = get_db_collection()
    count = db_collection.count_documents({})

    print(f"There are {count} teams in the DB.")
    print()

    print("Actions:")
    for _, name, description in actions:
        print(f"\t({name[0]}){name[1:]} \u2014 {description}")
