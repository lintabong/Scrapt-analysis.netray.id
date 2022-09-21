from pymongo import MongoClient


def connect_to_db(_mongoDBpass):
    mongoDBconn = f'mongodb+srv://lintabong:{_mongoDBpass}@cluster0.yxhdzte.mongodb.net/?retryWrites=true&w=majority'

    client = MongoClient(mongoDBconn)

    coll = client.Atmatech

    return coll

