from typing import IO

from bson import json_util

from .client import get_db_collection


def parse_to_db(json_fp: IO) -> None:
    db_collection = get_db_collection()

    json_as_dict = json_util.loads(
        json_fp.read()
    )

    for team in json_as_dict["teams"]:
        query = {"name": team["name"]}

        if db_collection.find_one(query):
            db_collection.replace_one(query, team)
            print("Replaced", team)
        else:
            db_collection.insert_one(team)
            print("Inserted", team)
