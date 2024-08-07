import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text: str) -> List[str]:
  # Remove special characters and digits
  text = re.sub(r'[^a-zA-Z\s]', '', text)
  
  # Tokenize
  tokens = word_tokenize(text.lower())
  
  # Remove stopwords and lemmatize
  tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
  
  return tokens

def extract_keywords(text: str, n: int = 10) -> List[str]:
  tokens = preprocess_text(text)
  word_freq = Counter(tokens)
  return [word for word, _ in word_freq.most_common(n)]

def generate_summary(text: str, n_sentences: int = 3) -> str:
  sentences = sent_tokenize(text)
  
  # Calculate TF-IDF
  vectorizer = TfidfVectorizer(stop_words='english')
  tfidf_matrix = vectorizer.fit_transform(sentences)
  
  # Calculate sentence scores
  sentence_scores = [(sentence, tfidf_matrix[i].sum()) for i, sentence in enumerate(sentences)]
  
  # Sort sentences by score and select top n
  summary_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)[:n_sentences]
  summary = ' '.join([sentence for sentence, score in summary_sentences])
  
  return summary

def extract_legal_entities(text: str) -> Dict[str, List[str]]:
  # This is a placeholder. In a real-world scenario, you'd use a named entity recognition model
  # trained on legal texts to extract entities like case names, statutes, etc.
  entities = {
      'case_names': [],
      'statutes': [],
      'legal_terms': []
  }
  
  # Implement entity extraction logic here
  
  return entities

def calculate_text_similarity(text1: str, text2: str) -> float:
  vectorizer = TfidfVectorizer(stop_words='english')
  tfidf_matrix = vectorizer.fit_transform([text1, text2])
  return ((tfidf_matrix * tfidf_matrix.T).A)[0, 1]
