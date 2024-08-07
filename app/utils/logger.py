import logging
import os
from app.config import Config

def setup_logger(name, log_file, level=logging.INFO):
  """Function to setup as many loggers as you want"""
  
  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
  
  if not os.path.exists(Config.LOG_DIR):
      os.makedirs(Config.LOG_DIR)
  
  handler = logging.FileHandler(os.path.join(Config.LOG_DIR, log_file))        
  handler.setFormatter(formatter)

  logger = logging.getLogger(name)
  logger.setLevel(level)
  logger.addHandler(handler)

  return logger

# Setup loggers
main_logger = setup_logger('main_logger', 'main.log')
model_logger = setup_logger('model_logger', 'model.log')
feature_logger = setup_logger('feature_logger', 'feature.log')
