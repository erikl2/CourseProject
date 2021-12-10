import pickle

with open('data/books_eng.pickle', 'rb') as f:
    books = pickle.load(f)

with open('data/titles.pickle', 'rb') as f:
    titles = pickle.load(f)

with open('data/summaries.pickle', 'rb') as f:
    summaries = pickle.load(f)

"""
The Light Between Oceans
Water for Elephants
And the Mountains Echoed
"""


print("Welcome to the Book Review Summarizer!")
run = True
while run:
    book_id = None
    while not book_id:
        title = input("Please enter a title: ")
        try:
            book_id = titles[title]
        except:
            print("Title not found. Please try again.")

    print("\n" + summaries[book_id])

    go = input("\nWould you like to view another title? (y/N)? ")
    if go == 'N':
        run = False