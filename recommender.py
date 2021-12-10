"""
Creates measures of similarity between books. Work in process (compute time).
"""

from google.colab import drive
import pickle
import pandas as pd
from collections import OrderedDict
from scipy import stats

drive.mount('/content/drive')

with open('/content/drive/MyDrive/books.pickle', 'rb') as f:
    books = pickle.load(f)

with open('/content/drive/MyDrive/reviews.pickle', 'rb') as f:
    reviews = pickle.load(f)

num_reviews = []
for book in books:
    num_reviews.append((len(books[book]['reviews']), book))
num_reviews.sort(reverse=True)
top1k = {}
for i in range(1000):
    if num_reviews[i][1] == 2657:
        print("yes!")
    top1k[num_reviews[i][1]] = 0

top_books = {}
for book in books:
    if book in top1k:
        top_books[book] = books[book].copy()

top_reviews = {}
for rev in reviews:
    if reviews[rev]['book_id'] in top_books:
        top_reviews[rev] = reviews[rev].copy()

user_ratings = OrderedDict()
for rev in top_reviews:
    user = top_reviews[rev]['user_id']
    user_ratings[user] = 0

for book in top_books:
    top_books[book]['user_ratings'] = []
for book in top_books:
    top_books[book]['book_corrs'] = {}

for book in top_books:
    top_books[book]['user_ratings'] = user_ratings.copy()

for rev in top_reviews:
    book_id = top_reviews[rev]['book_id']
    user = top_reviews[rev]['user_id']
    top_books[book_id]['user_ratings'][user] = top_reviews[rev]['rating']

for book_i in top_books:
    i_ratings = [] 
    for user in top_books[book_i]['user_ratings']:
        i_ratings.append(top_books[book_i]['user_ratings'][user])
    for book_j in top_books:
        j_ratings = [] 
        for user in top_books[book_j]['user_ratings']:
            j_ratings.append(top_books[book_i]['user_ratings'][user])
        top_books[book_i]['book_corrs'][book_j] = stats.pearsonr(i_ratings, j_ratings)


