import json
import os
    
def sentiment_sorting(combined_analysis_finals):
    if(not os.path.exists('data_analysis')):
        os.mkdir('data_analysis')
    
    for file in combined_analysis_finals:
        dir_filename = (file.split("_")[1][8:]) + "_sorting"
        current_sub = file.split("_")[1][8:]

        if not os.path.exists(dir_filename):
            os.mkdir(dir_filename)

        r = open(file, "r")
        posts = json.load(r)

        negative = []
        neutral = []
        positive = []

        for post in posts:
            titleSent = post['title_sentiment']
            discSent = post['description_sentiment']

            if abs(titleSent['compound']) >= abs(discSent['compound']):
                winner = titleSent
            else:
                winner = discSent

            compound_value = winner['compound']

            if compound_value == 0:
                neutral.append(post)
            elif compound_value > 0:
                positive.append(post)
            else:
                negative.append(post)

        a = open("data_analysis/"+current_sub+"_negatives.json", "w")
        json.dump(negative, a)

        b = open("data_analysis/"+current_sub+"_positives.json", "w")
        json.dump(positive, b)

        c = open("data_analysis/"+current_sub+"_neutrals.json", "w")
        json.dump(neutral, c)

    
if __name__ == '__main__':
    files = ["COMBINED_analysis/changemyview_analysis.json", "COMBINED_analysis/Conservative_analysis.json", "COMBINED_analysis/conspiracy_analysis.json", "COMBINED_analysis/democrats_analysis.json",
             "COMBINED_analysis/PoliticalDiscussion_analysis.json", "COMBINED_analysis/politics_analysis.json", "COMBINED_analysis/TrueReddit_analysis.json"]
    sentiment_sorting(files)
