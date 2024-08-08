
from sensor.configuration.mongo_db_connection import MongoDBClienct
from sensor.exception import SensorException
import sys, os
'''
if __name__ == '__main__':
    mongodb_client = MongoDBClienct()
    print("collection name: ",mongodb_client.database.list_collection_names())
    '''

def test_exception():
    try:
        x=1/0
    except Exception as e:
        raise SensorException(e, sys)

if __name__=='__main__':
    try:
        test_exception()
    except Exception as e:
        print(e)