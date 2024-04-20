import json
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import os

def extract_keyword_and_count(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    keywordDict = {}

    for word, pos in tagged:
        if pos.startswith('NN') or pos.startswith('JJ'):
            if word in keywordDict:
                keywordDict['b'] += 1
            else: 
                keywordDict[word] = 1
    return keywordDict

def get_keywords(comment_scrape_file_array):
    if(not os.path.exists('keyword_analysis')):
        os.mkdir('keyword_analysis')
    
    for file in comment_scrape_file_array:
        current_sub = file.split("_")[1][8:]
        r = open(file, "r")
        w = open("keyword_analysis/"+current_sub+"_analysis.json", "w")
        posts = json.load(r)
        scores = []
        for post in posts:
            title = post['title']
            title_keyword = extract_keyword_and_count(title)

            description = post['description']
            description_keyword = extract_keyword_and_count(description)

            for comments in post['comments']:
                comment_keyword = extract_keyword_and_count(comments)
                entry = dict(title=(title_keyword, title), description=(description_keyword, description), comment_keyword=(comment_keyword, comments))
                scores.append(entry)
        json.dump(scores, w)

if __name__ == '__main__':
    files = ["comment_scrapes/changemyview_comment_scrape.json", "comment_scrapes/Conservative_comment_scrape.json", "comment_scrapes/conspiracy_comment_scrape.json", "comment_scrapes/democrats_comment_scrape.json", "comment_scrapes/PoliticalDiscussion_comment_scrape.json", "comment_scrapes/politics_comment_scrape.json", "comment_scrapes/TrueReddit_comment_scrape.json"]
    get_keywords(files)
    # sia = SentimentIntensityAnalyzer()
    # print(sia.polarity_scores("hello"))