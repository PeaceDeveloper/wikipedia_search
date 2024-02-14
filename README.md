# Wikipedia Text Chunking, Vectorization and Search System

## Overview

This application is designed to perform the following tasks:

 - Extract a set of 10 articles from Wikipedia.
 - Chunk the text of each article and vectorize it using sentence transformers.
 - Store the embeddings of the text chunks in a Neo4j database.
 - Implement a search system based on cosine similarity, ranking the results based on relevance.

## Instructions

1. Rename the `.env.example` files inside the `neo4j` and `main` folders to `.env`.
2. Run `docker-compose up`.

Upon execution, the application will:

- Run a unit test to index the Wikipedia file chunks and search for a term.
- Start indexing chunks of ten Wikipedia files in parallel and search for a term every time a file is indexed.

For more information about the application's execution, refer to the log file located in the `main/logs` folder.