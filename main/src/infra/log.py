import logging

def configure():
    logging.basicConfig(filename='/app/logs/log.log', level= logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')