from langchain.graphs import Neo4jGraph
import logging
import os
import shutil
import traceback

NEO4J_URI="bolt://neo4j:7687"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD=os.environ.get("NEO4J_PASSWORD")

class DB():

    graph=None
    
    def __init__(self) -> None:
        self.graph = Neo4jGraph(
            url=NEO4J_URI,
            username=NEO4J_USERNAME,
            password=NEO4J_PASSWORD
        )
        
    def get_connection(self):
        return self.graph

    def undo_migrate(self, ignore_error = True):
        try:
            result = self.graph.query("""
                            MATCH (n)
                            DETACH DELETE n
                        """)
            logging.info(f'delete result {result}')
        except:
            logging.error(traceback.format_exc())
            if not ignore_error:
                raise
        try:                
            result = self.graph.query("""
                DROP INDEX wikipedia
            """)
            logging.info(f'drop index result {result}')
        except:
            logging.error(traceback.format_exc())
            if not ignore_error:
                raise
        try:
            shutil.rmtree(f"/app/files")
        except:
            logging.error(traceback.format_exc())
            if not ignore_error:
                raise
        

    def migrate(self, ignore_error = True):
        try:
            if os.environ.get('MODE') == 'DEV':
                self.undo_migrate(ignore_error)
            result = self.graph.query("""
                CALL db.index.vector.createNodeIndex(
                'wikipedia',
                'Chunk',
                'embedding',
                384,
                'cosine'
            )
            """)
            logging.info(f'create index result {result}')
        except:
            logging.error(traceback.format_exc())
            if not ignore_error:
                raise