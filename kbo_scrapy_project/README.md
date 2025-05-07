# KBO Scrapy Project

This project is a Scrapy spider designed to extract general information from the KBO (Kruispuntbank van Ondernemingen) website. The spider will gather various details about enterprises, including but not limited to:

- General information
- Functions
- Entrepreneurial capabilities
- Qualities
- Authorizations
- NACE codes
- Financial data
- Entity links
- External links

## Project Structure

The project has the following structure:

```
kbo_scrapy_project
├── kbo_scrapy_project
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── kbo_spider.py
├── scrapy.cfg
└── README.md
```

## Installation

To set up the project, ensure you have Python and Scrapy installed. You can install Scrapy using pip:

```bash
pip install scrapy
```

## Usage

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the spider using the following command:

```bash
scrapy crawl kbo_spider -a ondernemingsnummer=<NUMERO_ENTREPRISE>
```

Replace `<NUMERO_ENTREPRISE>` with the actual enterprise number you wish to scrape.

## Configuration

The project is configured to connect to a MongoDB database for storing the scraped data. Ensure that MongoDB is running and the connection settings in `settings.py` are correct.

## License

This project is open-source and available under the MIT License.