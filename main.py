# Importing the dotenv package to use environment variables
# This will help with not exposing sensitive info and credentials on the repo
from dotenv import load_dotenv
import os # helper package
load_dotenv()  # This line brings all environment variables from .env into os.environ

import json
import requests
from nltk.sentiment import SentimentIntensityAnalyzer

# Author: Adya

# TODO: This method extracts comment ID of posts from the scrape files
# TODO: Comment ID is in the permalink attribute
# TODO: for example, "/r/democrats/comments/1bsdtxg" for this permalink, "1bsdtxg"
# TODO: Return comment IDs as a String Array

# Function to extract comment IDs from JSON files
def getCommentIDs(files_to_scrape):
    # Initialize an empty list to store comment IDs
    comment_ids = []

    # Loop over each file in the list of files to scrape
    for file in files_to_scrape:
        # Open the file in read mode
        with open(file, 'r') as json_file:
            # Load the JSON data from the file
            data = json.load(json_file)
        
        # Loop over each child in the 'children' list of the 'data' dictionary
        for child in data['data']['children']:
            # Get the 'permalink' value from the 'data' dictionary of the child, return an empty string if 'permalink' is not present
            permalink = child['data'].get('permalink', '')
            # Split the permalink on '/' and concatenate the 3rd, 4th and 3rd last elements to form the comment ID
            comment_id = permalink.split('/')[2] + "/" + permalink.split('/')[3] + "/" + permalink.split('/')[-3]
            # Append the comment ID to the list of comment IDs
            comment_ids.append(comment_id)
        
        # Open a text file named 'comment_ids.txt' in write mode
        with open('comment_ids.txt', 'w') as output_file:
            # Loop over each comment ID in the list of comment IDs
            for comment_id in comment_ids:
                # Write the comment ID to the file followed by a newline character
                output_file.write(comment_id + '\n')
    
    # Return the list of comment IDs
    return comment_ids


######################################################################
# Author : Kru

#This function takes the general comment_id.txt file and creates new txt file for each subreddit
#This function serves as a helper for the commentScrapeBySubreddit function defined later
def commentIdBySubreddit(comment_ids_file):
    subreddits = [] #create list of subreddits to iterate
    r = open(comment_ids_file, "r") #open file given in parameter
    comments = r.readlines() #read each line from the txt file
    current_subbreddit = comments[0].split("/")[0] #define the first subreddit
    subreddits.append(current_subbreddit) #push sr to array
    if(not os.path.exists("comment_ids")): #if dir does not exist, create it
        os.mkdir("comment_ids")
    w = open("comment_ids/" + current_subbreddit+"_comment_ids.txt", "w") #write comment ids to its respective subreddit file
    for comment in comments: #iterate over each comment id line
        if(comment.split("/")[0] == current_subbreddit): #don't create new file if its the same sr
            w.write(comment) #write comment id to curr file
        else:
            current_subbreddit = comment.split("/")[0] #update sr name
            w = open("comment_ids/" + current_subbreddit+"_comment_ids.txt", "w") #create new file for the new sr
            w.write(comment) #write comment id to newly created file
            subreddits.append(current_subbreddit) #append the sr to sr array
            print("created comment_ids/" + current_subbreddit+"_comment_ids.txt")
    return subreddits # return sr array
######################################################################

######################################################################            
##Author: Kru
    #read comment_ids.txt, sort by subbreddit, and store each comment for that subreddit in a separate file
    #data = array of all comments including the op
    # each comment in data has an attribute called children
    # the first comment has a children that contains the title of the post
    # subsequent comments have a body attribute that constitue the comments of the post (excluding the title/op)
def commentScrapeBySubreddit(subreddit_comment_id_file_array, headers):
    if(not os.path.exists("comment_scrapes")): #if dir does not exist, create it
        os.mkdir("comment_scrapes")
    for comment_id_file in subreddit_comment_id_file_array: #iterate over each file in input array
        r = open(comment_id_file, 'r') #open the respective file
        comments = r.readlines() #read each line from opened file to get comment id
        current_sub = comments[0].split("/")[0] #extract current subreddit name
        w = open("comment_scrapes/"+current_sub+"_comment_scrape.json", "w") #create dump file for the current subreddit
        posts = [] #array to hold each post 
        for comment in comments: #iterate over each comment id in sub_comment_id_file
            data = requests.get("https://oauth.reddit.com/r/" + comment.strip(), headers=headers).json() #make API request to get the entire post
            title = data[0]['data']['children'][0]['data']['title'] #index the data to obtain the post title
            selftext = data[0]['data']['children'][0]['data']['selftext'] ##index the data to obtain the post description provided by OP
            time = data[0]['data']['children'][0]['data']['created']
            post_comments = [] #create comment array to store all comments and sub comments of the post
            for thread in data[1:]: #iterate over each thread within the post
                for subthread in thread['data']['children'][:-1]: #iterate over each sub thread
                    post_comments.append(subthread['data']['body']) #append each comment in subthread to post_comments_array
            entry = dict(title=title, description=selftext, time=time, comments=post_comments) #create a dict to hold the title, description, and ALL the comments of the post
            # print(entry) #was using this for testing
            posts.append(entry)
        json.dump(posts, w) #dump dict into the custom subreddit comment_scrape file
        print("Created comment_scrapes/"+current_sub+"_comment_scrape.json")
        r.close() #close fd
        w.close() #close fd
        
######################################################################

def rawScrape(headers):
##########################################################################################
# Author: Ashley
    # To run this program, uncomment the chunk of code using 'Ctrl/Cmd + /'
    # These lines scrape the top 100 most controversial posts from each subreddit into a json file
    f = open("scrape.json", "w")
    json.dump(requests.get("https://oauth.reddit.com/r/conspiracy/controversial", headers=headers,
    params={'limit': '100'}).json(), f)
    f.close()

    f = open("scrape1.json", "w")
    json.dump(requests.get("https://oauth.reddit.com/r/politics/controversial", headers=headers,
    params={'limit': '100'}).json(), f)
    f.close()

    f = open("scrape2.json", "w")
    json.dump(requests.get("https://oauth.reddit.com/r/TrueReddit/controversial", headers=headers,
    params={'limit': '100'}).json(), f)
    f.close()

    f = open("scrape3.json", "w")
    json.dump(requests.get("https://oauth.reddit.com/r/PoliticalDiscussion/controversial", headers=headers,
    params={'limit': '100'}).json(), f)
    f.close()

    f = open("scrape4.json", "w")
    json.dump(requests.get("https://oauth.reddit.com/r/changemyview/controversial", headers=headers,
    params={'limit': '100'}).json(), f)
    f.close()

    f = open("scrape5.json", "w")
    json.dump(requests.get("https://oauth.reddit.com/r/Conservative/controversial", headers=headers,
    params={'limit': '100'}).json(), f)
    f.close()

    f = open("scrape6.json", "w")
    json.dump(requests.get("https://oauth.reddit.com/r/democrats/controversial", headers=headers,
    params={'limit': '100'}).json(), f)
    f.close()

    #iterate over comment_id.txt file and look collect comment information into commentScrape.json
    r = open("comment_ids.txt", "r")
    w = open("commentScrape.json", "w")
    comments = r.readlines()
    for comment in comments:
        json.dump(requests.get("https://oauth.reddit.com/r/" + comment.strip(), headers=headers, params={'limit': '5'}).json(), w)
    r.close()
    w.close()

def dataCollection():
############################## --- API ACCESS --- ##############################
# Author: Ashley
    # set up to obtain access key
    CLIENT_ID = os.environ['CLIENT_ID']
    SECRET_KEY = os.environ['SECRET_KEY']
    import requests
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
        'grant_type': 'password',
        'username': os.environ['USERNAME'],
        'password': os.environ['PASSWORD']
    }
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'
    # print(headers)

    # test to make sure the token is taken, should print with exit code 0
    # print(requests.get("https://oauth.reddit.com/api/v1/me", headers=headers).json())
    print("############################################################")
    print("Welcome to our project!!")
    print("REDDIT NLP - Investigating Echo Chambers!")
    print("############################################################")
    print("Commencing Data Collection....")
    # print("Collecting raw data from Reddit API using API keys defined in .env file")
    # rawScrape(headers)
    files_to_scrape = ["scrape.json", "scrape1.json", "scrape2.json", "scrape3.json", "scrape4.json", "scrape5.json", "scrape6.json"]
    print("Getting comment Ids from general scrape file:")
    getCommentIDs(files_to_scrape)
    print("Comment Ids have been dumped to comment_ids.txt")
    print("############################################################")
    print("Creating subreddit file for every comment from the comment id file....")
    commentIdBySubreddit("comment_ids.txt")
    print("############################################################")
    #commentScrapeBySubreddit is called here so it can get the headers from auth token of API
    print("Scraping comments for every subreddit from the respective comment id file....")
    comment_id_files_array = ["comment_ids/changemyview_comment_ids.txt", "comment_ids/Conservative_comment_ids.txt", "comment_ids/conspiracy_comment_ids.txt", "comment_ids/democrats_comment_ids.txt", "comment_ids/PoliticalDiscussion_comment_ids.txt", "comment_ids/politics_comment_ids.txt", "comment_ids/TrueReddit_comment_ids.txt"]
    commentScrapeBySubreddit(comment_id_files_array, headers)
    print("############################################################")
    

import sentiment_analysis
import postPartitioning
import global_averageSentiment
import combined_SAKA
import charts
if __name__ == '__main__':
    dataCollection()
    sentiment_analysis.main()
    combined_SAKA.main()
    postPartitioning.main()
    global_averageSentiment.main()
    charts.main()
    
    
    
