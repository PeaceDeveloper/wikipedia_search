from model.Wikipedia import Wikipedia
import logging
from model.Vectorizer import Vectorizer
import traceback

class Indexer():

    vectorizer:Vectorizer

    def __init__(self, vectorizer) -> None:
        self.vectorizer = vectorizer
    
    def index(self, wiki_title, graph):
        result = f"{wiki_title} finished"
        try:
            logging.info(f'indexing {wiki_title}')
            wiki = Wikipedia(graph, self.vectorizer)
            wiki.save(wiki_title, 50)
            #fast test
            logging.info('****running fast test*****')
            results = wiki.search("What is data science?")
            logging.info(f'fast test results:\n{results}')
        except:
            logging.error(traceback.format_exc())
            result = f'{wiki_title} failed'
        return result
        