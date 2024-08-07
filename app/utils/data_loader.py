import os
import json
import pandas as pd
from typing import List, Dict, Any
from app.config import Config

def load_json_file(file_path: str) -> Dict[str, Any]:
  with open(file_path, 'r') as file:
      return json.load(file)

def load_csv_file(file_path: str) -> pd.DataFrame:
  return pd.read_csv(file_path)

def load_text_file(file_path: str) -> str:
  with open(file_path, 'r') as file:
      return file.read()

def load_cases(directory: str = Config.RAW_DATA_DIR) -> List[Dict[str, Any]]:
  cases = []
  for filename in os.listdir(directory):
      if filename.endswith('.json'):
          file_path = os.path.join(directory, filename)
          case = load_json_file(file_path)
          cases.append(case)
  return cases

def load_judgments(directory: str = Config.RAW_DATA_DIR) -> List[Dict[str, Any]]:
  judgments = []
  for filename in os.listdir(directory):
      if filename.endswith('.txt'):
          file_path = os.path.join(directory, filename)
          judgment_text = load_text_file(file_path)
          judgment_id = os.path.splitext(filename)[0]
          judgments.append({
              'id': judgment_id,
              'text': judgment_text
          })
  return judgments

def load_judge_data(file_path: str = os.path.join(Config.RAW_DATA_DIR, 'judges.csv')) -> pd.DataFrame:
  return load_csv_file(file_path)

def save_processed_data(data: Any, file_name: str, directory: str = Config.PROCESSED_DATA_DIR):
  if not os.path.exists(directory):
      os.makedirs(directory)
  
  file_path = os.path.join(directory, file_name)
  
  if file_name.endswith('.json'):
      with open(file_path, 'w') as file:
          json.dump(data, file)
  elif file_name.endswith('.csv'):
      if isinstance(data, pd.DataFrame):
          data.to_csv(file_path, index=False)
      else:
          pd.DataFrame(data).to_csv(file_path, index=False)
  else:
      with open(file_path, 'w') as file:
          file.write(str(data))
