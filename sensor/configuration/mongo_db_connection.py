import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()

class MongoDBClienct:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClienct.client is None:
                mongo_db_url = "enter url here"
                MongoDBClienct.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClienct.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e
