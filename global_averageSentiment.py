import json
import os
import statistics
    
def getAverageStructure():
    os_string = (os.getcwd() + "\data_analysis")
    new_string = os_string.replace("\\", "/")
    subname = ""
                                         
    dirpath = new_string

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
        
        x = file.split("\\")
        filename_data_dict[x[1]] = dataDict

    return filename_data_dict

def getPostKeywordStructure():
    os_string = (os.getcwd() + "\data_analysis")
    new_string = os_string.replace("\\", "/")
                                         
    dirpath = new_string
    files = [os.path.join(dirpath, file) for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]   

    if(not os.path.exists('subreddit_post_keywords')):
            os.mkdir('subreddit_post_keywords')

    for file in files:
        r = open(file, "r")
        posts = json.load(r)
        x = file.split("\\")
        current_file = x[1]
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
    os_string = (os.getcwd() + "\data_analysis")
    new_string = os_string.replace("\\", "/")
                                         
    dirpath = new_string
    files = [os.path.join(dirpath, file) for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]   

    if(not os.path.exists('subreddit_keywords')):
            os.mkdir('subreddit_comment_keywords')
    
    for file in files:
        r = open(file, "r")
        posts = json.load(r)
        x = file.split("\\")
        current_file = x[1]
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
    with open("Averages.txt", "w") as output_file:
        for file_name in allDataDict:
            commentAverageList = []
            post_average = 0
            fileDataDict = allDataDict[file_name]

            for postSentVal in fileDataDict:
                comment_average = statistics.mean(fileDataDict[postSentVal])
                post_average = statistics.mean(fileDataDict.keys())
                commentAverageList.append(comment_average)

            if commentAverageList == []:
                commentAverage = 0
            else: 
                commentAverage = statistics.mean(commentAverageList)
    
            output_file.write("-------" + file_name + " AVERAGES -------\n\n")
            output_file.write("Post Average: " + str(post_average) + "\n\n")
            output_file.write("Comment Average: " + str(commentAverage) + "\n\n")
            output_file.write("\n")

def printTop20PostKW():
    os_string = (os.getcwd() + "\subreddit_post_keywords")
    new_string = os_string.replace("\\", "/")
    dirpath = new_string
    files = [os.path.join(dirpath, file) for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]   
    
    with open("Top20PostKW.txt", "w", encoding='utf-8') as output_file:
        for file in files:
            x = file.split("\\")
            current_file = x[1]
            output_file.write("------ " + current_file + " Top Post Keywords ----------\n\n")
            r = open(file, "r")
            dict_data = json.load(r)

            sortedPostKeywords = sorted(dict_data.items(), key=lambda x: x[1], reverse=True)
            topKW = sortedPostKeywords[:24]
            for word in topKW:
                output_file.write("- " + word[0] + " | " + str(word[1]) + "\n")
            output_file.write("\n")

def printTop20CommentKW():
    os_string = (os.getcwd() + "\subreddit_comment_keywords")
    new_string = os_string.replace("\\", "/")

    dirpath = new_string
    files = [os.path.join(dirpath, file) for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]
    
    with open("Top20CommentKW.txt", "w") as output_file:
        for file in files:
            x = file.split("\\")
            current_file = x[1]
            output_file.write("------ " + current_file + " Top Comment Keywords ----------\n\n")
            r = open(file, "r")
            dict_data = json.load(r)

            sortedPostKeywords = sorted(dict_data.items(), key=lambda x: x[1], reverse=True)
            topKW = sortedPostKeywords[:24]
            for word in topKW:
                output_file.write("- " + word[0] + " | " + str(word[1]) + "\n")
            output_file.write("\n")

        
if __name__ == '__main__':
    getCommentKeywordStructure()
    printTop20CommentKW()
    
    getPostKeywordStructure()
    printTop20PostKW()
    
    x = getAverageStructure()
    computeAverages(x)
