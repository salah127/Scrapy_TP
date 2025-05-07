import scrapy

class TPItem(scrapy.Item):
    enterprise_number = scrapy.Field()
    general_info = scrapy.Field()
    functions = scrapy.Field()
    entrepreneurial_capacities = scrapy.Field()
    qualities = scrapy.Field()
    authorizations = scrapy.Field()
    nace_codes = scrapy.Field()
    financial_data = scrapy.Field()
    entity_links = scrapy.Field()
    external_links = scrapy.Field()