import json
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


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
    
        

if __name__ == '__main__':
    files = ["comment_scrapes/changemyview_comment_scrape.json", "comment_scrapes/Conservative_comment_scrape.json", "comment_scrapes/conspiracy_comment_scrape.json", "comment_scrapes/democrats_comment_scrape.json", "comment_scrapes/PoliticalDiscussion_comment_scrape.json", "comment_scrapes/politics_comment_scrape.json", "comment_scrapes/TrueReddit_comment_scrape.json"]
    SAKA(files)
