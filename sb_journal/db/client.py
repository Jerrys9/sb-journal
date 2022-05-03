from pymongo import MongoClient

_db_client = None


def get_db_client():
    global _db_client

    if _db_client is None:
        _db_client = MongoClient()

    return _db_client


def get_db_collection():
    return get_db_client().sb_journal.teams
