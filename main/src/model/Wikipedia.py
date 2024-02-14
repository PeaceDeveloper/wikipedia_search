from model.SentenceTransformerVectorizer import Vectorizer
import wikipedia
from os.path import exists
import logging
import os

class Wikipedia():

    id:int
    title:str
    content:str
    chunks = None
    path:str
    vectorizer:Vectorizer
    graph = None

    def __init__(self, graph, vectorizer) -> None:
        self.graph = graph
        self.vectorizer = vectorizer
        
    def save(self, wiki_title:str, chunk_size:int):
        saved = False
        self.title = wiki_title
        self.path = f"/app/files/{self.title}.txt"
        if not exists(self.path):
            page = wikipedia.page(wiki_title)
            self.id = page.pageid
            self.content = page.content
            self.chunks = [{'text':el, 'embedding': self.vectorizer.encode(el)} for
                    el in page.content.split("\n\n") if len(el) > chunk_size]            
            try:
                with open(self.path, 'w') as f:
                    self.graph.query("""
                        UNWIND $data AS row
                        CREATE (c:Chunk {text: row.text})
                        WITH c, row
                        CALL db.create.setVectorProperty(c, 'embedding', row.embedding)
                        YIELD node
                        RETURN distinct 'done'
                        """, {'data': self.chunks})
                    f.write(f"{self.title}\n\n{self.content}")
                    logging.info(f'{self.path} indexed')
                    saved = True
            except:
                os.remove(self.path)
        else:
            logging.info(f'{self.path} already indexed')            
        return saved

    def search(self, query, k=3):

        # ranking the results based on relevance. It's ordering by score desc
        vector_search = """
            WITH $embedding AS e
            CALL db.index.vector.queryNodes('wikipedia',$k, e) yield node, score
            RETURN node.text AS result
            ORDER BY score DESC
            LIMIT 3
            """
        embedding = self.vectorizer.encode(query)
        context = self.graph.query(
            vector_search, {'embedding': embedding, 'k': k})        
        results = [el['result'] for el in context]
        return results