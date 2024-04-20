import json
from nltk.sentiment import SentimentIntensityAnalyzer
import os


def sentiment(comment_scrape_file_array):
    sia = SentimentIntensityAnalyzer()
    if(not os.path.exists('ENHANCED_sentiment_analyses')):
        os.mkdir('ENHANCED_sentiment_analyses')
    
    for file in comment_scrape_file_array:
        current_sub = file.split("_")[1][8:]
        r = open(file, "r")
        w = open("sentiment_analyses/"+current_sub+"_analysis.json", "w")
        posts = json.load(r)
        scores = []
        for post in posts:
            title = post['title']
            title_sentiment = sia.polarity_scores(title)

            description = post['description']
            description_sentiment = sia.polarity_scores(description)

            for comments in post['comments']:
                sentiment_scores = sia.polarity_scores(comments)
                entry = dict(title=(title_sentiment, title), description=(description_sentiment, description), comment_sentiment=sentiment_scores)
                scores.append(entry)
        json.dump(scores, w)
    
        

if __name__ == '__main__':
    files = ["comment_scrapes/changemyview_comment_scrape.json", "comment_scrapes/Conservative_comment_scrape.json", "comment_scrapes/conspiracy_comment_scrape.json", "comment_scrapes/democrats_comment_scrape.json", "comment_scrapes/PoliticalDiscussion_comment_scrape.json", "comment_scrapes/politics_comment_scrape.json", "comment_scrapes/TrueReddit_comment_scrape.json"]
    sentiment(files)
    # sia = SentimentIntensityAnalyzer()
    # print(sia.polarity_scores("hello"))