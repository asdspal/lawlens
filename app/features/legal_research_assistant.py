from app.models.inlegalbert import InLegalBERT
from app.models.graph_rag import GraphRAG
from app.utils.text_processor import extract_keywords, generate_summary

class LegalResearchAssistant:
  def __init__(self, inlegalbert: InLegalBERT, graph_rag: GraphRAG):
      self.inlegalbert = inlegalbert
      self.graph_rag = graph_rag
      self.document_database = []

  def add_document(self, doc_id, doc_text, doc_type):
      embedding = self.inlegalbert.get_embeddings(doc_text)
      keywords = extract_keywords(doc_text)
      summary = generate_summary(doc_text)
      
      self.document_database.append({
          'id': doc_id,
          'text': doc_text,
          'type': doc_type,
          'embedding': embedding,
          'keywords': keywords,
          'summary': summary
      })
      
      self.graph_rag.add_node(doc_id, {
          'embedding': embedding,
          'text': doc_text,
          'type': doc_type,
          'keywords': keywords,
          'summary': summary
      })

  def search(self, query, n=10):
      query_embedding = self.inlegalbert.get_embeddings(query)
      results = self.graph_rag.query(query_embedding, n)
      return results

  def generate_research_summary(self, query):
      relevant_docs = self.search(query)
      # Implement logic to synthesize information from relevant documents
      # and generate a comprehensive research summary
      pass

  def cross_reference(self, doc_id):
      doc = next((d for d in self.document_database if d['id'] == doc_id), None)
      if doc:
          related_docs = self.graph_rag.query(doc['embedding'], n=5)
          return related_docs
      return []

  def suggest_related_statutes(self, case_text):
      # Implement logic to suggest related statutes based on case text
      pass
