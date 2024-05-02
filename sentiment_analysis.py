import json
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import matplotlib.pyplot as plt
from scipy import stats
from datetime import datetime 


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
        print("Created sentiment_analyses/"+current_sub+"_analysis.json")
    
def overTime(sentiment_analysis_file_array):
    if (not os.path.exists('over_time')):
        os.mkdir('over_time')
    # for every subreddit
    for file in sentiment_analysis_file_array:
        sub_name = file.split("_")[1][8:]
        r = open(file, "r")
        comments = json.load(r)  # load in the sentiment labelled text
        time = []
        yPos = []
        yNeg = []
        timeUnchanged = []

        # for every post in that subreddit
        for comment in comments:
            # add to the relevant lists
            yPos.append(comment['sentiment_scores']['pos'])
            yNeg.append(comment['sentiment_scores']['neg'])
            # convert timestamp to proper format, but still save the original timestamp
            convertedTime = datetime.fromtimestamp(comment['time'])
            timeUnchanged.append(comment['time'])
            time.append(convertedTime)

        # print the graph for positive sentiment over time
        plt.scatter(time, yPos, c='black')
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        sub_reddit_name = file.split("_")[1][9:]
        # print(sub_reddit_name)
        plt.title('Positive Sentiment Over Time in r/' + sub_reddit_name)  # split gets the subreddit name
        plt.suptitle('Correlation score: ' + str(stats.pearsonr(timeUnchanged, yPos).statistic))
        # Save graph to a file
        plt.savefig('over_time' + sub_name + "_positive.png", dpi=300)
        print("Created over_time" + sub_name + "_positive.png")

        # print the graph for negative sentiment over time
        plt.scatter(time, yNeg, c='black')
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.title('Negative Sentiment Over Time in r/' + sub_reddit_name)  # split gets the subreddit name
        plt.suptitle('Correlation score: ' + str(stats.pearsonr(timeUnchanged, yNeg).statistic))
        # Save graph to a file
        plt.savefig('over_time' + sub_name + "_negative.png", dpi=300)
        print("Created over_time" + sub_name + "_negative.png")

def main():
    files = ["comment_scrapes/changemyview_comment_scrape.json", "comment_scrapes/Conservative_comment_scrape.json", "comment_scrapes/conspiracy_comment_scrape.json", "comment_scrapes/democrats_comment_scrape.json", "comment_scrapes/PoliticalDiscussion_comment_scrape.json", "comment_scrapes/politics_comment_scrape.json", "comment_scrapes/TrueReddit_comment_scrape.json"]
    files_sa = ["sentiment_analyses/changemyview_analysis.json", "sentiment_analyses/Conservative_analysis.json", "sentiment_analyses/conspiracy_analysis.json", "sentiment_analyses/democrats_analysis.json", "sentiment_analyses/PoliticalDiscussion_analysis.json", "sentiment_analyses/politics_analysis.json", "sentiment_analyses/TrueReddit_analysis.json"]
    print("Analysing sentiment for each comment from each subreddit!")
    sentiment(files)
    print("############################################################")
    print("Creating over time sentiment graphs...")
    overTime(files_sa)
    print("############################################################")

if __name__ == '__main__':
    main()
