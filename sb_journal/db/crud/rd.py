from sb_journal.db.client import get_db_collection
from .validators import validator_exists


def _rd(method, name):
    db_collection = get_db_collection()

    if name is None:
        query = {}
    else:
        query = {"name": name}

    return getattr(db_collection, method)(query)


def get(name=None):
    return _rd("find", name)


def delete(name=None):
    if name is not None:
        validator_exists(name)

    return _rd("delete_many", name)
