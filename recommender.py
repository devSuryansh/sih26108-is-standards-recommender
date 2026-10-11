"""TF-IDF retrieval over a SAMPLE catalogue (made-up entries, not real BIS standards)."""
import json, re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, path="data/sample_standards.json"):
        self.items = json.load(open(path))
        self.vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), sublinear_tf=True)
        self.X = self.vec.fit_transform([f"{i['title']} {i['title']} {i['keywords']}" for i in self.items])

    def recommend(self, spec, k=5):
        q = self.vec.transform([spec]); sims = cosine_similarity(q, self.X)[0]
        vocab = self.vec.get_feature_names_out(); qn = q.nonzero()[1]
        out = []
        for idx in sims.argsort()[::-1][:k]:
            if sims[idx] <= 0: break
            row = self.X[idx].nonzero()[1]
            matched = sorted(vocab[j] for j in set(qn) & set(row))
            out.append({**self.items[idx], "score": round(float(sims[idx]), 3), "matched_terms": matched})
        return out
