import scrapy
import csv
from TP.items import TPItem

class KboSpider(scrapy.Spider):
    name = "kbo_spider"
    allowed_domains = ["kbopub.economie.fgov.be"]

    def start_requests(self):
        # Read enterprise numbers from the CSV file
        print("salaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah")
        with open('enterprise.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            i=0
            for row in reader:
                i=i+1
                if i<3:
                    transformed = row['EnterpriseNumber']
                    enterprise_number = transformed.replace(".", "")
                    print("Row:", enterprise_number)
                    url = f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={enterprise_number}&lang=fr"
                    
                    
                    
                    yield scrapy.Request(url, self.parse, meta={'enterprise_number': enterprise_number})

    def parse(self, response):
        item = TPItem()
        item['enterprise_number'] = response.meta['enterprise_number']
        table_div_text = response.xpath('//div[@id="table"]//text()').getall()
        
        table_rows = response.xpath('//div[@id="table"]//tr')
        content= table_rows
        general_info = []
        functions = []
        entrepreneurial_capacities = []
        qualities = [] 
        authorizations = []
        nace_codes = []
        financial_data = []
        entity_links = []
        external_links = []
        for row in table_rows:
            row_text = row.xpath('.//text()').getall()
            if row_text==['Fonctions']:
                break
            content = content[1:]
            if row_text and row_text!=['\xa0', '\xa0'] and row_text!=['\xa0']:
                general_info.append(row_text)
        for row in content:
            row_text = row.xpath('.//text()').getall()
            if row_text==['Capacités entrepreneuriales - ambulant - exploitant forain']:
                break
            content = content[1:]
            if row_text and row_text!=['\xa0', '\xa0'] and row_text!=['\xa0']:
                functions.append(row_text)
        for row in content:
            row_text = row.xpath('.//text()').getall()
            if row_text==['Qualités']:
                break
            content = content[1:]
            if row_text and row_text!=['\xa0', '\xa0'] and row_text!=['\xa0']:
                entrepreneurial_capacities.append(row_text)
        for row in content:
            row_text = row.xpath('.//text()').getall()
            if row_text==['Autorisations']:
                break
            content = content[1:]
            if row_text and row_text!=['\xa0', '\xa0'] and row_text!=['\xa0']:
                qualities.append(row_text)
        for row in content:
            row_text = row.xpath('.//text()').getall()
            if row_text==['Activités TVA Code Nacebel version 2025(1)']:
                break
            content = content[1:]
            print("row_text", row_text)
            if row_text and row_text!=['\xa0', '\xa0'] and row_text!=['\xa0']:
                authorizations.append(row_text)
        for row in content:
            row_text = row.xpath('.//text()').getall()
            if row_text==['Données financières']:
                break
            content = content[1:]
        for row in content:
            row_text = row.xpath('.//text()').getall()
            if row_text==['Liens entre entités']:
                break
            content = content[1:]
            if row_text and row_text!=['\xa0', '\xa0'] and row_text!=['\xa0']:
                nace_codes.append(row_text)
            
                
        item['general_info'] = general_info
        # item['general_info'] = self.extract_general_info(response)
        item['functions'] = functions
        item['entrepreneurial_capacities'] = entrepreneurial_capacities
        item['qualities'] = qualities
        item['authorizations'] =  authorizations
        item['nace_codes'] = nace_codes
        item['financial_data'] = self.extract_section(response, "Données financières")
        item['entity_links'] = self.extract_section(response, "Liens entre entités")
        item['external_links'] = self.extract_section(response, "Liens externes")
        yield item

    def extract_general_info(self, response):
        return {
            "name": response.xpath('//h1/text()').get(),
            "address": response.xpath('//div[@class="address"]/text()').get(),
            "status": response.xpath('//div[@class="status"]/text()').get(),
        }

    def extract_section(self, response, section_name):
        section = response.xpath(f'//h2[contains(text(), "{section_name}")]/following-sibling::div')
        return section.xpath('.//text()').getall()

    def extract_nace_codes(self, response):
        nace_section = response.xpath('//h2[contains(text(), "NACE")]/following-sibling::div')
        return nace_section.xpath('.//text()').getall()