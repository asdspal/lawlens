import unittest
from app.models.inlegalbert import InLegalBERT
from app.models.graph_rag import GraphRAG

class TestInLegalBERT(unittest.TestCase):
  def setUp(self):
      self.model = InLegalBERT()

  def test_get_embeddings(self):
      text = "This is a test sentence."
      embeddings = self.model.get_embeddings(text)
      self.assertIsNotNone(embeddings)
      self.assertEqual(embeddings.shape[1], 768)  # Assuming BERT base model

class TestGraphRAG(unittest.TestCase):
  def setUp(self):
      self.graph_rag = GraphRAG()

  def test_add_node(self):
      node_id = "test_node"
      data = {"text": "Test text", "embedding": [0.1] * 768}
      self.graph_rag.add_node(node_id, data)
      self.assertIn(node_id, self.graph_rag.graph.nodes)

  def test_query(self):
      # Add some test nodes
      for i in range(5):
          self.graph_rag.add_node(f"node_{i}", {"text": f"Test text {i}", "embedding": [0.1] * 768})

      query_embedding = [0.1] * 768
      results = self.graph_rag.query(query_embedding, n=3)
      self.assertEqual(len(results), 3)

if __name__ == '__main__':
  unittest.main()

