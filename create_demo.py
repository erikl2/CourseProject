import pickle
from transformers import pipeline
import contextlib
summarizer = pipeline("summarization")


with open('data/books_eng.pickle', 'rb') as f:
    books = pickle.load(f)

with open('data/reviews.pickle', 'rb') as f:
    reviews = pickle.load(f)

with open('data/titles.pickle', 'rb') as f:
    titles = pickle.load(f)

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

    return reviews_summary


summaries = {}
for book_id in [19012815, 631096, 21387605]:  # 18170778
    summaries[book_id] = make_summ(book_id)

with open('summaries.pickle', 'wb') as handle:
    pickle.dump(summaries, handle, protocol=pickle.HIGHEST_PROTOCOL)
