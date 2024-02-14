
from model.Vectorizer import Vectorizer
from sentence_transformers import SentenceTransformer

# singleton pattern
class SentenceTransformerVectorizer(Vectorizer):

    _instance = None

    def __init__(self):
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        super().__init__(model)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def encode(self, text:str):
        return self.model.encode(text, convert_to_tensor=False)