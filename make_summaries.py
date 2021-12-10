"""
Creates summaries of the top 5 most helpful positive and top 5 most helpful negative reviews (in English).
"""

import pickle
from google.colab import drive
!pip install langdetect
from langdetect import detect
!pip install transformers
from transformers import pipeline

drive.mount('/content/drive')

with open('/content/drive/MyDrive/books_eng.pickle', 'rb') as f:
    books = pickle.load(f)

with open('/content/drive/MyDrive/reviews.pickle', 'rb') as f:
    reviews = pickle.load(f)

titles = {}
for book in books:
    titles[books[book]['title']] = book
with open('/content/drive/MyDrive/titles.pickle', 'wb') as f:
    pickle.dump(titles, f, protocol=pickle.HIGHEST_PROTOCOL)


for book in books:
    pos_sorted = []
    neg_sorted = []
    for rev in books[book]['reviews']:
        if reviews[rev]['rating'] > 3.5:
            pos_sorted.append((reviews[rev]['votes'], rev))
        else:
            neg_sorted.append((reviews[rev]['votes'], rev))
    pos_sorted.sort(reverse=True)
    neg_sorted.sort(reverse=True)
    pos = []
    neg = []
    for rev in pos_sorted:
        try:
            if detect(reviews[rev[1]]['review_text']) == 'en':
                pos.append(rev)
                if len(pos) >= 5:
                    break
        except:
            pass
    for rev in neg_sorted:
        try:
            if detect(reviews[rev[1]]['review_text']) == 'en':
                neg.append(rev)
                if len(neg) >= 5:
                    break
        except:
            pass
    books[book]['top_5_pos'] = []
    books[book]['top_5_neg'] = []
    for i in range(5):
        try:
            books[book]['top_5_pos'].append(pos[i][1])
            books[book]['top_5_neg'].append(neg[i][1])
        except:
            pass


summarizer = pipeline("summarization")


def make_summ(book_id):
    
    positives = []
    critical = []

    for i in range(5):
        try:
            review_id = books[book_id]['top_5_pos'][i]
            review = reviews[review_id]['review_text']
            maxlen = min(len(review), 15)
            summary = summarizer(review, max_length=maxlen, min_length=2, do_sample=False)[0]['summary_text']
            positives.append(summary)
        except:
            pass

    for i in range(5):
        try:
            review_id = books[book_id]['top_5_neg'][i]
            review = reviews[review_id]['review_text']
            maxlen = min(len(review), 15)
            summary = summarizer(review, max_length=maxlen, min_length=2, do_sample=False)[0]['summary_text']
            critical.append(summary)
        except:
            pass

    reviews_summary = ""
    reviews_summary += books[book_id]['title']
    reviews_summary += f"\nAverage rating: {books[book_id]['rating']}"
    reviews_summary += "\n\nPositive review summaries: "
    for i in range(5):
        try:
            reviews_summary += "\n * " + positives[i]
        except:
            break
    reviews_summary += "\n\nCritical review summaries: "
    for i in range(5):
        try:
            reviews_summary += "\n * " + critical[i]
        except:
            break

    books[book_id]['reviews_summary'] = reviews_summary

for book in books:
    make_summ(book)