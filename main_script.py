from . import scraper

import os

links = scraper.run()

scraper.download_files(os.path.dirname(__file__), links)

