import matplotlib.pyplot as plt
import networkx as nx

def create_trend_visualization(trend_data):
  years = list(trend_data.keys())
  counts = list(trend_data.values())
  
  plt.figure(figsize=(12, 6))
  plt.plot(years, counts, marker='o')
  plt.title('Legal Trend Analysis')
  plt.xlabel('Year')
  plt.ylabel('Number of Cases')
  plt.grid(True)
  
  return plt

def visualize_graph(graph, highlight_nodes=None):
  pos = nx.spring_layout(graph)
  plt.figure(figsize=(12, 8))
  nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8, font_weight='bold')
  
  if highlight_nodes:
      nx.draw_networkx_nodes(graph, pos, nodelist=highlight_nodes, node_color='red', node_size=700)
  
  plt.title('Document Relationship Graph')
  return plt
