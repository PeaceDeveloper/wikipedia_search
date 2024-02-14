# Wikipedia Article Chunker and Search System

## Overview

This application is specific to:

- Taking a set of 10 articles from Wikipedia
- Chunking the text
- Vectorizing the text using sentence transformers
- Storing the embeddings of the text chunks in Neo4j
- Implementing a search system based on cosine similarity

## Instructions

1. Rename the `.env.example` files inside the `neo4j` and `main` folders to `.env`.
2. Run `docker-compose up`.

Upon execution, the application will:

- Run a unit test to index the Wikipedia file chunks and search for a term.
- Start indexing chunks of ten Wikipedia files in parallel and search for a term every time a file is indexed.

For more information about the application's execution, refer to the log file located in the `main/logs` folder.