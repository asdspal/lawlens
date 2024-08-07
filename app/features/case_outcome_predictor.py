from app.models.inlegalbert import InLegalBERT
from app.models.graph_rag import GraphRAG
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import numpy as np

class CaseOutcomePredictor:
  def __init__(self, inlegalbert: InLegalBERT, graph_rag: GraphRAG):
      self.inlegalbert = inlegalbert
      self.graph_rag = graph_rag
      self.model = RandomForestClassifier()
      self.case_database = []

  def add_case(self, case_id, case_text, outcome):
      embedding = self.inlegalbert.get_embeddings(case_text)
      self.case_database.append({
          'id': case_id,
          'text': case_text,
          'embedding': embedding,
          'outcome': outcome
      })
      self.graph_rag.add_node(case_id, {'embedding': embedding, 'text': case_text, 'outcome': outcome})

  def train_model(self):
      X = np.array([case['embedding'].numpy().flatten() for case in self.case_database])
      y = np.array([case['outcome'] for case in self.case_database])
      
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
      
      self.model.fit(X_train, y_train)
      
      y_pred = self.model.predict(X_test)
      print(classification_report(y_test, y_pred))

  def predict_outcome(self, case_text):
      embedding = self.inlegalbert.get_embeddings(case_text).numpy().flatten()
      prediction = self.model.predict([embedding])[0]
      confidence = self.model.predict_proba([embedding]).max()
      
      return prediction, confidence

  def explain_prediction(self, case_text):
      # Implement logic to explain the factors influencing the prediction
      pass

  def find_similar_cases(self, case_text, n=5):
      embedding = self.inlegalbert.get_embeddings(case_text)
      similar_cases = self.graph_rag.query(embedding, n)
      return similar_cases
