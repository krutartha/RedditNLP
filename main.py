#### Importing the dotenv package to use environment variables
## This will help with not exposing sensitive info and credentials on the repo
from dotenv import load_dotenv
import os ##helper package
load_dotenv()  # This line brings all environment variables from .env into os.environ



import json
import requests

# TODO: Adya this method should extract comment ID of posts from the scrape files
# TODO: Comment ID is in the permalink attribute
# TODO: for example, "/r/democrats/comments/1bsdtxg" for this permalink, "1bsdtxg"
# TODO: Return comment IDs as a String Array

# Function to extract comment IDs from JSON files
def getCommentIDs(files_to_scrape):
    comment_ids = []
    for file in files_to_scrape:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
        
        for child in data['data']['children']:
            permalink = child['data'].get('permalink', '')
            comment_id = permalink.split('/')[2] + "/" + permalink.split('/')[3] + "/" + permalink.split('/')[-3]
            comment_ids.append(comment_id)
        
        # Write comment IDs to a text file
        with open('comment_ids.txt', 'w') as output_file:
            for comment_id in comment_ids:
                output_file.write(comment_id + '\n')
    return comment_ids

# List of files to extract comment IDs from
files_to_scrape = ["scrape.json", "scrape1.json", "scrape2.json", "scrape3.json", "scrape4.json", "scrape5.json", "scrape6.json"]
getCommentIDs(files_to_scrape)


def dataCollection():
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
    print(headers)

    # test to make sure the token is taken, should print with exit code 0
    print(requests.get("https://oauth.reddit.com/api/v1/me", headers=headers).json())


    # To run this program, uncomment the chunk of code from lines 63 to 161 using 'Ctrl/Cmd + /'
    # f = open("scrape.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/conspiracy/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # f = open("scrape1.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/politics/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # f = open("scrape2.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/TrueReddit/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # f = open("scrape3.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/PoliticalDiscussion/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # f = open("scrape4.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/changemyview/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # f = open("scrape5.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/Conservative/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # f = open("scrape6.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/democrats/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # iterate over comment_id.txt file and look collect comment information into commentScrape.json
    # r = open("comment_ids.txt", "r")
    # w = open("commentScrape.json", "w")
    # comments = r.readlines()
    # for comment in comments:
    #     json.dump(requests.get("https://oauth.reddit.com/r/" + comment.strip(), headers=headers, params={'limit': '5'}).json(), w)
    # r.close()
    # w.close()


if __name__ == '__main__':
    dataCollection()
