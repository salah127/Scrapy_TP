from pymongo import MongoClient

class MongoDBPipeline:
    def open_spider(self, spider):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['kbo_data']
        self.collection = self.db['enterprises']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item