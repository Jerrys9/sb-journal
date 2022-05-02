from sb_catalog.storage.client import get_db_collection


def get(name=None):
    db_collection = get_db_collection()

    if name is None:
        query = {}
    else:
        query = {"name": name}

    return db_collection.find(query)


def add(name, **other_data):
    if list(get(name)):
        raise ValueError ("the team already exists in the DB")

    db_collection = get_db_collection()

    name_data = {"name": name}

    return db_collection.insert_one(
        {**name_data, **other_data}
    )


def edit(name, **other_data):
    if not list(get(name)):
        raise ValueError ("the team does not exist in the DB")

    db_collection = get_db_collection()

    name_data = {"name": name}

    return db_collection.replace_one(
        name_data,
        {**name_data, **other_data},
    )


def delete(name=None):
    if not list(get(name)):
        raise ValueError ("the team does not exist in the DB")

    db_collection = get_db_collection()

    if name is None:
        query = {}
    else:
        query = {"name": name}

    return db_collection.delete_many(query)
