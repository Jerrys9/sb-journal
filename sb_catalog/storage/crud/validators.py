from sb_catalog.storage.client import get_db_collection


def _exists(name):
    return bool(
        get_db_collection().find_one({"name": name})
    )


def validator_exists(name):
    if _exists(name):
        return

    raise ValueError("the team doesn't exist in the DB")


def validator_nexists(name):
    if not _exists(name):
        return

    raise ValueError("the team already exists in the DB")
