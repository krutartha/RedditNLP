import json
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import matplotlib.pyplot as plt


def extract_keyword_and_count(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    keywordDict = {}

    for word, pos in tagged:
        if pos.startswith('NN') or pos.startswith('JJ'):
            if word in keywordDict:
                keywordDict[word] += 1
            else: 
                keywordDict[word] = 1
    return keywordDict

def SAKA(comment_scrape_file_array):
    sia = SentimentIntensityAnalyzer()
    if(not os.path.exists('COMBINED_analysis')):
        os.mkdir('COMBINED_analysis')
    
    for file in comment_scrape_file_array:
        current_sub = file.split("_")[1][8:]
        r = open(file, "r")
        w = open("COMBINED_analysis/"+current_sub+"_analysis.json", "w")
        posts = json.load(r)
        scores = []

        for post in posts:
            title = post['title']
            title_sentiment = sia.polarity_scores(title)
            title_keyword = extract_keyword_and_count(title)

            description = post['description']
            description_sentiment = sia.polarity_scores(description)
            description_keyword = extract_keyword_and_count(description)

            for comments in post['comments']:
                comment_sentiment = sia.polarity_scores(comments)
                comment_keyword = extract_keyword_and_count(comments)
                entry = dict(title=title, description=description, comment=comments,
                             title_sentiment=title_sentiment, description_sentiment=description_sentiment, comment_sentiment=comment_sentiment, 
                             title_keywords=title_keyword, description_keywords=description_keyword, comment_keywords=comment_keyword)
                scores.append(entry)
        json.dump(scores, w)
        print("Created COMBINED_analysis/"+current_sub+"_analysis.json")

def createHistogram():
    files = ["changemyview_analysis.json", "Conservative_analysis.json", "conspiracy_analysis.json", "democrats_analysis.json", "PoliticalDiscussion_analysis.json", "politics_analysis.json", "TrueReddit_analysis.json"]
    if(not os.path.exists('histogram')):
        os.mkdir('histogram')

    plt.figure(figsize=(10, 6))

    for file in files:
        with open("COMBINED_analysis/" + file, "r") as f:
            data = json.load(f)

        # Extract the compound sentiment scores for the titles
        title_scores = [post['title_sentiment']['compound'] for post in data]

        # Create a histogram of the scores
        plt.hist(title_scores, bins=20, edgecolor='black', alpha=0.5, label=file.split('_')[0])

    plt.title("Sentiment scores for post titles in various subreddits")
    plt.xlabel("Sentiment score")
    plt.ylabel("Number of posts")
    plt.legend()
    plt.savefig("histogram/combined_hist.png", dpi=300)
    print("Created histogram plot at histogram/combined_hist.png")

    
def main():
    print("Extracting keywords and combining sentiment analysis!")
    files = ["comment_scrapes/changemyview_comment_scrape.json", "comment_scrapes/Conservative_comment_scrape.json", "comment_scrapes/conspiracy_comment_scrape.json", "comment_scrapes/democrats_comment_scrape.json", "comment_scrapes/PoliticalDiscussion_comment_scrape.json", "comment_scrapes/politics_comment_scrape.json", "comment_scrapes/TrueReddit_comment_scrape.json"]
    SAKA(files)
    print("############################################################")
    print("Creating Histogram for combined analysis!")
    createHistogram()
    print("############################################################")

if __name__ == '__main__':
    main()
