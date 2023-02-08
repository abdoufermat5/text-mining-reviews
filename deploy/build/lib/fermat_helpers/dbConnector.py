import pandas as pd
import pymongo as pymongo


class DBConnector:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://data_miner:DataMining123@dataminingcluster.2cswb3o.mongodb.net"
                                          "/?retryWrites=true&w=majority", connect=False)
        self.db = self.client.dataMiningDB
        self.collection = self.db.amazonCollection

    def change_collection(self, collection):
        self.collection = self.db[collection]

    def is_collection_exists(self, collection):
        return collection in self.db.list_collection_names()

    def drop_collection(self, collection):
        self.db.drop_collection(collection)

    def create_collection(self, collection):
        # check if collection exists
        if collection in self.db.list_collection_names():
            self.change_collection(collection)
            print("Collection already exists")
            print("Collection changed to: " + collection)
        else:
            self.db.create_collection(collection)
            self.change_collection(collection)

    def insert(self, data):
        self.collection.insert_one(data)

    def insert_many(self, data):
        self.collection.insert_many(data, bypass_document_validation=True)

    def find(self, query):
        return self.collection.find(query)

    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, data):
        self.collection.update_one(query, data)

    def delete(self, query):
        self.collection.delete_one(query)

    def delete_many(self, query):
        self.collection.delete_many(query)

    def count(self, query):
        return self.collection.count_documents(query)

    def count_all(self):
        return self.collection.count_documents({})

    def get_all(self):
        return self.collection.find({})

    def get_base_data(self):
        df = pd.DataFrame(list(self.get_all()))
        df = df.drop(columns=['_id'])
        return df

    def get_train_data(self):
        # change collection
        self.change_collection('amazonTrainingCollection')
        df = pd.DataFrame(list(self.get_all()))
        df = df.drop(columns=['_id'])
        return df

    def get_test_data(self):
        # change collection
        self.change_collection('amazonTestCollection')
        df = pd.DataFrame(list(self.get_all()))
        df = df.drop(columns=['_id'])
        return df
