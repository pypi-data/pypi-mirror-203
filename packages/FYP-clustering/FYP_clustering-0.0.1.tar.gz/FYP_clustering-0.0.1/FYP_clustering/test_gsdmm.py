from unittest import TestCase
from gsdmm.mgp import MovieGroupProcess
import numpy
import unittest
from sklearn.feature_extraction.text import TfidfVectorizer

def setUp(self):
        numpy.random.seed(47)

def tearDown(self):
        numpy.random.seed(None)

def compute_V(self, texts):
        V = set()
        for text in texts:
            for word in text:
                V.add(word)
        return len(V)

def test_short_text(self):
    texts = [
        "where the red dog lives",
        "red dog lives in the house",
        "blue cat eats mice",
        "monkeys hate cat but love trees",
        "green cat eats mice",
        "orange elephant never forgets",
        "orange elephant must forget",
        "monkeys eat banana",
        "monkeys live in trees",
        "elephant",
        "cat",
        "dog",
        "monkeys"
        ]

    texts = [text.split() for text in texts]
    V = self.compute_V(texts)
    mgp = MovieGroupProcess(K=30, n_iters=100, alpha=0.2, beta=0.01)
    y = mgp.fit(texts, V)
    self.assertTrue(len(set(y))<10)
    self.assertTrue(len(set(y))>3)
    print(y)

    def get_top_words(corpus, n):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(corpus)
        feature_names = vectorizer.get_feature_names()
        top_words_list = []
        for i in range(len(corpus)):
            tfidf_scores = tfidf_matrix[i].toarray()[0]
            word_scores = [(feature_names[j], tfidf_scores[j]) for j in range(len(feature_names))]
            sorted_word_scores = sorted(word_scores, key=lambda x: x[1], reverse=True)
            top_words = [word for (word, score) in sorted_word_scores[:n]]
            top_words_list.append(top_words)
        return top_words_list

    lists =  [ "where the red dog lives red dog lives in the house dog"      ]
    tw = get_top_words(lists, 2)

    print(tw)
        
def Run():
    test_short_text()
    return "Finished！"
        

    