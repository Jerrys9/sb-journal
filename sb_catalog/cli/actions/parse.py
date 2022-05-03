from sb_catalog.db.parser import parse_to_db


def parse():
    filename = input("Enter JSON filename: ")
    try:
        with open(filename) as fp:
            parse_to_db(fp)
    except Exception as e:
        print("Error:", e)
