import json
import os
import statistics
    
def getAverageStructure():
    dirpath = "/Users/sensh/Desktop/RedditNLP-main/data_analysis"
    files = [os.path.join(dirpath, file) for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]   
    filename_data_dict = {}
    
    for file in files:
        r = open(file, "r")
        posts = json.load(r)
        
        dataDict = {}
        
        for post in posts:
            titleSent = post['title_sentiment']
            discSent = post['description_sentiment']

            if abs(titleSent['compound']) >= abs(discSent['compound']):
                winner = titleSent
            else:
                winner = discSent
                
            compound_value = winner['compound']
            comment_sentiment = post['comment_sentiment']
            comm_sent_val = comment_sentiment['compound']

            if compound_value in dataDict:
                dataDict[compound_value].append(comm_sent_val)
            else:
                dataDict[compound_value] = [comm_sent_val]
                
        filename_data_dict[file[50:]] = dataDict

    return filename_data_dict

def computeAverages(allDataDict):
    # {'changemyview_negatives.json': {-0.8836: [-0.895, -0.5647, 0.3182, -0.8823],  -0.9995: [0.6124, -0.6808, 0.7003, -0.9704, -0.8315] }
    i = 0
    
    for file_name in allDataDict:
        i += 1
        commentAverageList = []
        post_average = 0
        fileDataDict = allDataDict[file_name]

        for postSentVal in fileDataDict:
            comment_average = statistics.mean( fileDataDict[postSentVal] )
            post_average = statistics.mean(fileDataDict.keys())
            commentAverageList.append(comment_average)

        commentAverage= statistics.mean(commentAverageList)

        print("-------" + file_name + " AVERAGES ------- " + str(i) + "\n")
        print("Post Average: " + str(post_average) + "\n")
        print("Comment Average: " + str(commentAverage) + "\n")
        print ("\n")
        




            
if __name__ == '__main__':
    files = ["COMBINED_analysis/changemyview_analysis.json", "COMBINED_analysis/Conservative_analysis.json", "COMBINED_analysis/conspiracy_analysis.json", "COMBINED_analysis/democrats_analysis.json",
             "COMBINED_analysis/PoliticalDiscussion_analysis.json", "COMBINED_analysis/politics_analysis.json", "COMBINED_analysis/TrueReddit_analysis.json"]
    result2 = getAverageStructure()
    computeAverages(result2)

