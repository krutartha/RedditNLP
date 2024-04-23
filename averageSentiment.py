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

            comment_sentiment = post['comment_sentiment']
            
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

def getPostKeywordStructure():
    dirpath = "/Users/sensh/Desktop/RedditNLP-main/data_analysis"
    files = [os.path.join(dirpath, file) for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]   

    if(not os.path.exists('subreddit_post_keywords')):
            os.mkdir('subreddit_post_keywords')

    for file in files:
        r = open(file, "r")
        posts = json.load(r)
        current_file = file[50:]
        postKW_dict = {}

        w = open("subreddit_post_keywords/"+current_file+"_post_keywords.json", "w")
        
        for post in posts:
            #title of post for ID 
            post_title = ((post['title'])[:25])
            
            #gets keyword dicts
            titleKeyword = post['title_keywords']
            discKeyword = post['description_keywords']

            #goes trough kw dict adds title kw to postKW dict
            for key, value in titleKeyword.items():
                key = key.lower()
                if len(key) <= 2 or key == chr:
                    continue
                else: 
                    if key in postKW_dict:
                        postKW_dict[key] += value
                    else: 
                            postKW_dict[key] = value
            
            #goes trough kw dict adds decsr. kw's to postKW dict
            for key, value in discKeyword.items():
                key = key.lower()
                if len(key) <= 2 or key == chr:
                    continue
                else: 
                    if key in postKW_dict:
                        postKW_dict[key] += value
                    else: 
                            postKW_dict[key] = value
                
        json.dump(postKW_dict, w)

def getCommentKeywordStructure():
    dirpath = "/Users/sensh/Desktop/RedditNLP-main/data_analysis"
    files = [os.path.join(dirpath, file) for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]   

    if(not os.path.exists('subreddit_keywords')):
            os.mkdir('subreddit_comment_keywords')
    
    for file in files:
        r = open(file, "r")
        posts = json.load(r)
        current_file = file[50:]
        commentKW_Dict = {}
    
        w = open("subreddit_comment_keywords/"+current_file+"_comment_keywords.json", "w")
        
        for post in posts:
            #title of post for ID 
            post_title = ((post['title'])[:25])
            
            #gets keyword dicts
            commentKeyword = post['comment_keywords']

            #goes trough comment kw dict adds comment kw to commentKW dict
            for key, value in commentKeyword.items():
                key = key.lower()
                if len(key) <= 2 or key == chr:
                    continue
                else: 
                    if key in commentKW_Dict:
                        commentKW_Dict[key] += value
                    else: 
                        commentKW_Dict[key] = value
                
        # filename_kw_dict[file[50:]] = dataDict
        json.dump(commentKW_Dict, w)

def computeAverages(allDataDict):
    # {'changemyview_negatives.json': {-0.8836: [-0.895, -0.5647, 0.3182, -0.8823],  -0.9995: [0.6124, -0.6808, 0.7003, -0.9704, -0.8315] }

    for file_name in allDataDict:
        commentAverageList = []
        post_average = 0
        fileDataDict = allDataDict[file_name]

        for postSentVal in fileDataDict:
            comment_average = statistics.mean( fileDataDict[postSentVal] )
            post_average = statistics.mean(fileDataDict.keys())
            commentAverageList.append(comment_average)

        commentAverage= statistics.mean(commentAverageList)

        print("-------" + file_name + " AVERAGES -------\n")
        print("Post Average: " + str(post_average) + "\n")
        print("Comment Average: " + str(commentAverage) + "\n")
        print ("\n")

def printTop20PostKW():
    dirpath = "/Users/sensh/Desktop/RedditNLP-main/subreddit_post_keywords"
    files = [os.path.join(dirpath, file) for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]   
    
    for file in files:
        current_file = file[59:90]
        print("------ " + current_file + " Top Post Keywords ----------\n")
        r = open(file, "r")
        dict = json.load(r)

        sortedPostKeywords = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        topKW = sortedPostKeywords[:24]
        for word in topKW:
            print("- " + word[0] + " | " + str(word[1]))
        print("\n")

def printTop20CommentKW():
    dirpath = "/Users/sensh/Desktop/RedditNLP-main/subreddit_comment_keywords"
    files = [os.path.join(dirpath, file) for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]   

    for file in files:
        current_file = file[53:95]
        print("------ " + current_file + " Top Comment Keywords ----------\n")
        r = open(file, "r")
        dict = json.load(r)

        sortedPostKeywords = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        topKW = sortedPostKeywords[:24]
        for word in topKW:
            print("- " + word[0] + " | " + str(word[1]))
        print("\n")
        
if __name__ == '__main__':
    getCommentKeywordStructure()
    getPostKeywordStructure()
    printTop20PostKW()
    print("\n\n\n\n")
    printTop20CommentKW()
    # getPostKeywordStructure()
    # getPostKeywordStructure()
