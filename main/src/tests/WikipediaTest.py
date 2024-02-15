import unittest
from model.Wikipedia import Wikipedia
from infra.db import DB
from model.SentenceTransformerVectorizer import SentenceTransformerVectorizer

class TestWikipedia():
    WIKI_TITLE = "Data science"

    def test_connection(self):
        new4j_db = DB()
        new4j_db.migrate()
        graph = new4j_db.get_connection()
        vectorizer = SentenceTransformerVectorizer.instance()
        wiki = Wikipedia(graph, vectorizer)
        wiki.save(self.WIKI_TITLE, 50)
        results = wiki.search("What is data science?")
        assert len(results) > 0