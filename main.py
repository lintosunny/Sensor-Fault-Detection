from sensor.configuration.mongo_db_connection import MongoDBClienct

if __name__ == '__main__':
    mongodb_client = MongoDBClienct()
    print("collection name: ",mongodb_client.database.list_collection_names())