# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import json
import os

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
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)

        plt.savefig('word_clouds/'+sub_name+".png", dpi=300)

        
if __name__ == '__main__':
    files = ["COMBINED_analysis/changemyview_analysis.json", "COMBINED_analysis/Conservative_analysis.json", "COMBINED_analysis/conspiracy_analysis.json", "COMBINED_analysis/democrats_analysis.json", "COMBINED_analysis/PoliticalDiscussion_analysis.json",  "COMBINED_analysis/politics_analysis.json", "COMBINED_analysis/TrueReddit_analysis.json"]
    makeWordClouds(files)