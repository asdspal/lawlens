import os

class Config:
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  DATA_DIR = os.path.join(BASE_DIR, 'data')
  RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
  PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
  KNOWLEDGE_GRAPH_DIR = os.path.join(DATA_DIR, 'knowledge_graph')
  LOG_DIR = os.path.join(BASE_DIR, 'logs')
