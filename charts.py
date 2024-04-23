# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import json
import os
import numpy as np

def makeWordClouds(file_array):
    if(not os.path.exists('word_clouds')):
        os.mkdir('word_clouds')
    for file in file_array:
        sub_name = file.split("/")[1].split(".")[0][:-9].lower()
        print(sub_name)
        r = open(file, "r")
        json_file = json.load(r)

        comment_words = ''
        stopwords = set(STOPWORDS)
        words = []
        
        for post in json_file:
            for attribute in post['title_keywords']:
                # print(attribute, post['title_keywords'][attribute])
                if(attribute != sub_name):
                    words.append(attribute)
            for attribute in post['description_keywords']:
                # print(attribute, post['description_keywords'][attribute])
                if(attribute != sub_name):
                    words.append(attribute)
            for attribute in post['comment_keywords']:
                # print(attribute, post['comment_keywords'][attribute])
                if(attribute != sub_name):
                    words.append(attribute)
        for i in range(len(words)):
            words[i] = words[i].lower().strip()
        # print(words)
        comment_words += " ".join(words)
        wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)
        # plot and save the WordCloud image	
        plt.clf()				 
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)

        plt.savefig('word_clouds/'+sub_name+".png", dpi=300)

def makePieChart(file_array):
    if(not os.path.exists('pie_charts')):
        os.mkdir('pie_charts')
    for file in file_array:
        sub_name = file.split("_")[1][9:].lower()
        # print(sub_name)
        r = open(file, "r")
        json_file = json.load(r)
        average_positive = 0
        average_negative = 0
        average_neutral = 0
        average_compound = 0
        
        for post in json_file:
            average_positive += post["sentiment_scores"]["pos"]
            average_negative += post["sentiment_scores"]["neg"]
            average_neutral += post["sentiment_scores"]["neu"]
            average_compound += post["sentiment_scores"]["compound"]
        average_positive = average_positive/len(json_file)
        average_negative = average_negative/len(json_file)
        average_neutral = average_neutral/len(json_file)
        average_compound = average_compound/len(json_file)
        
        plt.clf()	
        y = np.array([average_positive, average_negative, average_neutral])
        labels = ["Positive", "Negative", "Neutral"]
        colors = ["Green", "Red", "#e6e600"]
        plt.pie(y, labels=labels, colors=colors, autopct="%.2f%%")
        plt.legend(title=sub_name)
        plt.savefig('pie_charts/'+sub_name+".png", dpi=300)
        
if __name__ == '__main__':
    combined_files = ["COMBINED_analysis/changemyview_analysis.json", "COMBINED_analysis/Conservative_analysis.json", "COMBINED_analysis/conspiracy_analysis.json", "COMBINED_analysis/democrats_analysis.json", "COMBINED_analysis/PoliticalDiscussion_analysis.json",  "COMBINED_analysis/politics_analysis.json", "COMBINED_analysis/TrueReddit_analysis.json"]
    comment_files = ["sentiment_analyses/changemyview_analysis.json", "sentiment_analyses/Conservative_analysis.json", "sentiment_analyses/conspiracy_analysis.json", "sentiment_analyses/democrats_analysis.json", "sentiment_analyses/PoliticalDiscussion_analysis.json", "sentiment_analyses/politics_analysis.json", "sentiment_analyses/TrueReddit_analysis.json"]
    makeWordClouds(combined_files)
    # makePieChart(comment_files)