import src.pre_clean as clean
import src.wordcloud as wc
import src.plotting as pt
import pandas as pd
import numpy as np
from sklearn.decomposition import NMF, LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from sklearn.manifold import MDS

def get_vectorizers(df_collapsed):
    tfidf_vectorizer = TfidfVectorizer(min_df=5, max_df=0.80, stop_words='english', lowercase=True, token_pattern='[a-zA-Z\-][a-zA-Z\-]{2,}')

    count_vectorizer = CountVectorizer(min_df=5, max_df=0.80, stop_words='english', lowercase=True, token_pattern='[a-zA-Z\-][a-zA-Z\-]{2,}')

    data_tfidf_vectorized = tfidf_vectorizer.fit_transform(df_collapsed)
    # feature_names = tfidf_vectorizer.get_feature_names()
    data_count_vectorized = count_vectorizer.fit_transform(df_collapsed)

    return data_tfidf_vectorized, data_count_vectorized

if __name__ == '__main__':
    pass
