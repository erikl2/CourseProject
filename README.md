# CS 410 Project - Book Review Summarizer

#### [Project presentation](https://youtu.be/3asJjsafpQw)

My project goal was to create a program that outputs summaries of book reviews. The program takes a book title and returns the average rating, followed by
summaries of the five most helpful positive reviews and the five most helpful negative reviews, to give a quick overview of why people may or may not have
enjoyed the book.

My first challenge was finding a suitable dataset. It was difficult to find datasets that included full texts of book reviews, but I was fortunate to find
the [UCSD Book Graph dataset](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home)

One of the main challenges of working with large datasets is having sufficient memory to process them. I was unable to work with the full set of 2.36M books and 15.7M reviews due to a lack of computing resources. Thankfully, I was able to work with a subset of around 300,000 history and authobiographical books along with 2M reviews. I used Google Colab for some additional resources and saved the essential parts of the data into pickle format (shown in the /data and /preprocessing folders).

I filtered the reviews to English language reviews only. I further selected the top five most helpful positive reviews and top five most helpful negative reviews for each book using the Goodreads votes (shown in make_summaries.py). I used a Huggingface Transformers summarization pipeline to create summaries of each of these reviews.

### Future Improvements
I exceeded the time I had allocated for this project, but learned a lot and saw some promising results. I hope to expand on these with future improvements.

The results from the summarizer, while helpful, could be improved. It could be better fine-tuned to the dataset, which might yield sharper results.

I am working on an additional recommender system (shown in recommender.py) designed to show a list of similar books. The correlation calculations to rank similarity are very computationally intensive, so I'm working with a further subset of the data.

I am also considering making a web-based frontend to provide more visual interest, but I am pleased with the functionality of the current command line interface.