from sb_journal.db.client import get_db_collection
from .validators import validator_exists, validator_nexists


def add(name, **other_data):
    validator_nexists(name)

    db_collection = get_db_collection()

    name_data = {"name": name}

    return db_collection.insert_one(
        {**name_data, **other_data}
    )


def edit(name, **other_data):
    validator_exists(name)

    db_collection = get_db_collection()

    name_data = {"name": name}

    return db_collection.replace_one(
        name_data,
        {**name_data, **other_data},
    )
