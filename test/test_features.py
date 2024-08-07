import unittest
from unittest.mock import MagicMock
from app.features.legal_precedent_explorer import LegalPrecedentExplorer
from app.features.judgment_summarizer import JudgmentSummarizer

class TestLegalPrecedentExplorer(unittest.TestCase):
  def setUp(self):
      self.inlegalbert_mock = MagicMock()
      self.graph_rag_mock = MagicMock()
      self.explorer = LegalPrecedentExplorer(self.inlegalbert_mock, self.graph_rag_mock)

  def test_add_case(self):
      self.explorer.add_case("case1", "This is a test case", ["case2", "case3"])
      self.graph_rag_mock.add_node.assert_called_once()
      self.assertEqual(len(self.explorer.case_citation_network.nodes), 1)
      self.assertEqual(len(self.explorer.case_citation_network.edges), 2)

class TestJudgmentSummarizer(unittest.TestCase):
  def setUp(self):
      self.inlegalbert_mock = MagicMock()
      self.graph_rag_mock = MagicMock()
      self.summarizer = JudgmentSummarizer(self.inlegalbert_mock, self.graph_rag_mock)

  def test_summarize_judgment(self):
      judgment_text = "This is a test judgment. It has multiple sentences. We want to summarize it."
      summary = self.summarizer.summarize_judgment(judgment_text, num_sentences=2)
      self.assertIsInstance(summary, str)
      self.assertTrue(len(summary.split('.')) <= 2)

if __name__ == '__main__':
  unittest.main()
