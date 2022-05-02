from sb_catalog.storage.client import get_db_collection


def get(name=None):
    db_collection = get_db_collection()

    if name is None:
        query = {}
    else:
        query = {"name": name}

    return db_collection.find(query)


def delete(name=None):
    db_collection = get_db_collection()

    if name is None:
        query = {}
    else:
        query = {"name": name}

    return db_collection.delete_many(query)
