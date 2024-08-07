import streamlit as st
from app.models.inlegalbert import InLegalBERT
from app.models.graph_rag import GraphRAG
from app.features.legal_precedent_explorer import LegalPrecedentExplorer
from app.features.judgment_summarizer import JudgmentSummarizer
from app.features.legal_trend_analyzer import LegalTrendAnalyzer
from app.features.case_outcome_predictor import CaseOutcomePredictor
from app.features.legal_research_assistant import LegalResearchAssistant
from app.features.constitutional_interpreter import ConstitutionalInterpreter
from app.features.judge_profile_analyzer import JudgeProfileAnalyzer
from app.utils.logger import main_logger

def main():
  st.title("Legal LLM Application")

  try:
      # Initialize models and features
      inlegalbert = InLegalBERT()
      graph_rag = GraphRAG()
      legal_precedent_explorer = LegalPrecedentExplorer(inlegalbert, graph_rag)
      judgment_summarizer = JudgmentSummarizer(inlegalbert, graph_rag)
      legal_trend_analyzer = LegalTrendAnalyzer(inlegalbert, graph_rag)
      case_outcome_predictor = CaseOutcomePredictor(inlegalbert, graph_rag)
      legal_research_assistant = LegalResearchAssistant(inlegalbert, graph_rag)
      constitutional_interpreter = ConstitutionalInterpreter(inlegalbert, graph_rag)
      judge_profile_analyzer = JudgeProfileAnalyzer(inlegalbert, graph_rag)

      menu = ["Home", "Legal Precedent Explorer", "Judgment Summarizer", "Legal Trend Analyzer", 
              "Case Outcome Predictor", "Legal Research Assistant", "Constitutional Interpreter", 
              "Judge Profile Analyzer"]
      choice = st.sidebar.selectbox("Select a feature", menu)

      if choice == "Home":
          st.write("Welcome to the Legal LLM Application. Choose a feature from the sidebar to get started.")

      elif choice == "Legal Precedent Explorer":
          st.subheader("Legal Precedent Explorer")
          query = st.text_input("Enter your legal query:")
          if st.button("Search Precedents"):
              try:
                  results = legal_precedent_explorer.query_legal_precedents(query)
                  st.write(results)
              except Exception as e:
                  main_logger.error(f"Error in Legal Precedent Explorer: {str(e)}")
                  st.error("An error occurred while processing your request. Please try again.")

      # Add similar try-except blocks for other features...

  except Exception as e:
      main_logger.error(f"Unhandled exception in main application: {str(e)}")
      st.error("An unexpected error occurred. Please try again later.")

if __name__ == "__main__":
  main()
