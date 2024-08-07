from transformers import AutoTokenizer, AutoModel

class InLegalBERT:
  def __init__(self):
      self.tokenizer = AutoTokenizer.from_pretrained("law-ai/InLegalBERT")
      self.model = AutoModel.from_pretrained("law-ai/InLegalBERT")

  def get_embeddings(self, text):
      encoded_input = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
      output = self.model(**encoded_input)
      return output.last_hidden_state
