

import asyncio
import traceback
from infra.db import DB
import logging
import infra.log as log
from tasks.Indexer import Indexer
import concurrent.futures
import os
from model.SentenceTransformerVectorizer import SentenceTransformerVectorizer
import wikipedia

log.configure()
WIKI_PAGES = wikipedia.search('data science', results=10, suggestion=False)

async def main():
    try:
        new4j_db = DB()
        new4j_db.migrate()
        graph = new4j_db.get_connection()
        vectorizer = SentenceTransformerVectorizer.instance()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(Indexer(vectorizer).index, WIKI_PAGE, graph) for WIKI_PAGE in WIKI_PAGES]
            for future in concurrent.futures.as_completed(results):
                result = future.result()
                logging.info(f"Task result:{result}")
    except:
        logging.warn('Fail')
        logging.error(traceback.format_exc())
    else:
        logging.info('Finish')

asyncio.run(main())