import json
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import matplotlib.pyplot as plt


def sentiment(comment_scrape_file_array):
    sia = SentimentIntensityAnalyzer()
    if(not os.path.exists('sentiment_analyses')):
        os.mkdir('sentiment_analyses')
    for file in comment_scrape_file_array:
        current_sub = file.split("_")[1][8:]
        r = open(file, "r")
        w = open("sentiment_analyses/"+current_sub+"_analysis.json", "w")
        posts = json.load(r)
        scores = []
        for post in posts:
            title = post['title']
            description = post['description']
            cummulative_comment = ''
            for comments in post['comments']:
                cummulative_comment += comments
            sentiment_scores = sia.polarity_scores(cummulative_comment)
            time = post['time']
            entry = dict(title=title, description=description, time=time, sentiment_scores=sentiment_scores)
            scores.append(entry)
        json.dump(scores, w)
    
def overTime(sentiment_analysis_file_array):
    # for every subreddit
    for file in sentiment_analysis_file_array:
        r = open(file, "r")
        comments = json.load(r)  # load in the sentiment labelled text
        time = []
        yPos = []
        yNeg = []

        # for every post in that subreddit
        for comment in comments:

            # add to the relevant lists
            yPos.append(comment['sentiment_scores']['pos'])
            yNeg.append(comment['sentiment_scores']['neg'])
            time.append(comment['time'])

        # print the graph for positive sentiment over time
        plt.plot(time, yPos)
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.title('Positive Sentiment Over Time in r/', file.split("_")[1][8:])  # split gets the subreddit name

        # print the graph for negative sentiment over time
        plt.plot(time, yNeg)
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.title('Negative Sentiment Over Time in r/', file.split("_")[1][8:])  # split gets the subreddit name        

if __name__ == '__main__':
    files = ["comment_scrapes/changemyview_comment_scrape.json", "comment_scrapes/Conservative_comment_scrape.json", "comment_scrapes/conspiracy_comment_scrape.json", "comment_scrapes/democrats_comment_scrape.json", "comment_scrapes/PoliticalDiscussion_comment_scrape.json", "comment_scrapes/politics_comment_scrape.json", "comment_scrapes/TrueReddit_comment_scrape.json"]
    files_sa = ["sentiment_analyses/changemyview_analysis.json", "sentiment_analyses/Conservative_analysis.json", "sentiment_analyses/conspiracy_analysis.json", "sentiment_analyses/democrats_analysis.json", "sentiment_analyses/PoliticalDiscussion_analysis.json", "sentiment_analyses/politics_analysis.json", "sentiment_analyses/TrueReddit_analysis.json"]
    sentiment(files)
    overTime(files_sa)
    # sia = SentimentIntensityAnalyzer()
    # print(sia.polarity_scores("hello"))
