from app.models.inlegalbert import InLegalBERT
from app.models.graph_rag import GraphRAG
from app.utils.text_processor import extract_keywords, generate_summary
from collections import defaultdict

class JudgeProfileAnalyzer:
  def __init__(self, inlegalbert: InLegalBERT, graph_rag: GraphRAG):
      self.inlegalbert = inlegalbert
      self.graph_rag = graph_rag
      self.judge_profiles = defaultdict(lambda: {
          'judgments': [],
          'legal_areas': defaultdict(int),
          'citation_count': 0,
          'average_judgment_length': 0
      })

  def add_judgment(self, judge_name, judgment_text, case_id, legal_area, date):
      embedding = self.inlegalbert.get_embeddings(judgment_text)
      judgment = {
          'text': judgment_text,
          'case_id': case_id,
          'legal_area': legal_area,
          'date': date,
          'embedding': embedding
      }
      self.judge_profiles[judge_name]['judgments'].append(judgment)
      self.judge_profiles[judge_name]['legal_areas'][legal_area] += 1
      self.judge_profiles[judge_name]['average_judgment_length'] = (
          (self.judge_profiles[judge_name]['average_judgment_length'] * (len(self.judge_profiles[judge_name]['judgments']) - 1) +
           len(judgment_text)) / len(self.judge_profiles[judge_name]['judgments'])
      )
      
      self.graph_rag.add_node(f"{judge_name}_{case_id}", {
          'type': 'judgment',
          'judge': judge_name,
          'text': judgment_text,
          'case_id': case_id,
          'legal_area': legal_area,
          'date': date,
          'embedding': embedding
      })

  def analyze_judge_profile(self, judge_name):
      profile = self.judge_profiles[judge_name]
      top_legal_areas = sorted(profile['legal_areas'].items(), key=lambda x: x[1], reverse=True)[:5]
      
      return {
          'name': judge_name,
          'total_judgments': len(profile['judgments']),
          'top_legal_areas': top_legal_areas,
          'citation_count': profile['citation_count'],
          'average_judgment_length': profile['average_judgment_length']
      }

  def compare_judges(self, judge1, judge2):
      profile1 = self.analyze_judge_profile(judge1)
      profile2 = self.analyze_judge_profile(judge2)
      
      # Implement comparison logic here
      # This could involve comparing their top legal areas, citation counts, etc.

  def analyze_legal_philosophy(self, judge_name):
      judgments = self.judge_profiles[judge_name]['judgments']
      all_text = " ".join([j['text'] for j in judgments])
      keywords = extract_keywords(all_text, n=20)
      
      # Implement more sophisticated analysis of legal philosophy
      # This could involve topic modeling, sentiment analysis, etc.
      
      return {
          'keywords': keywords,
          # Add more analysis results here
      }

  def identify_influential_judgments(self, judge_name, top_n=5):
      # Implement logic to identify the most influential judgments
      # This could be based on citation count, impact on future cases, etc.
      pass
