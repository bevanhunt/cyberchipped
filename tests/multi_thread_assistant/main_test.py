from .main import main
import os
import pymongo


def test_main():
    if os.getenv("MONGO_URL") is not None:
        client = pymongo.MongoClient(os.getenv("MONGO_URL"))
        db = client[os.getenv("MONGO_DB")][os.getenv("MONGO_COLLECTION")]
        db.drop()
    os.remove("cyberchipped.db") if os.path.exists("cyberchipped.db") else None
    assert main() == "The result of adding 1 and 1 together is 2."
