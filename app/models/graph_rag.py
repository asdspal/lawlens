import networkx as nx
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class GraphRAG:
  def __init__(self):
      self.graph = nx.Graph()
      self.embeddings = {}

  def add_node(self, node_id, data):
      self.graph.add_node(node_id, **data)
      self.embeddings[node_id] = data['embedding']

  def add_edge(self, node1_id, node2_id, weight=1):
      self.graph.add_edge(node1_id, node2_id, weight=weight)

  def query(self, query_embedding, n=10):
      similarities = {}
      for node_id, embedding in self.embeddings.items():
          similarity = cosine_similarity(query_embedding.reshape(1, -1), embedding.reshape(1, -1))[0][0]
          similarities[node_id] = similarity
      
      top_nodes = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:n]
      
      results = []
      for node_id, similarity in top_nodes:
          node_data = self.graph.nodes[node_id]
          results.append({
              'id': node_id,
              'text': node_data['text'],
              'similarity': similarity,
              **{k: v for k, v in node_data.items() if k not in ['text', 'embedding']}
          })
      
      return results

  def get_subgraph(self, node_ids):
      return self.graph.subgraph(node_ids)
