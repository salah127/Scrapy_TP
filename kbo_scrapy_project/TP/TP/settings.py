BOT_NAME = 'TP'

SPIDER_MODULES = ['TP.spiders']
NEWSPIDER_MODULE = 'TP.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
    'TP.pipelines.MongoDBPipeline': 300,
}

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'kbo_data'