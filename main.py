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
def getCommentIDs(file_to_scrape):
    comment_ids = []
    for file in file_to_scrape:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
        
        for child in data['data']['children']:
            permalink = child['data'].get('permalink', '')
            comment_id = permalink.split('/')[-3]  # -3 to find the the commendIDs in the permalink. Also, it ends with '/'
            comment_ids.append(comment_id)
        
        # Write comment IDs to a text file
        with open('comment_ids.txt', 'w') as output_file:
            for comment_id in comment_ids:
                output_file.write(comment_id + '\n')

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

    # TODO: Adya, keep these scrapes commented unless you find something wrong with the JSON files. I just kept them
    #  in here for presentation purposes

    # To run this program, uncomment the chunk of code from lines 63 to 161 using 'Ctrl/Cmd + /'
    # f = open("scrape.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/conspiracy/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # TODO: Adya, when you are done with your getCommentsIDs function, you can uncomment all of these comment loops
    #  and run once to fill files. Afterwards,  comment them again so that we don't exceed our data usage
    # c = getCommentIDs("scrape.json")
    # file_num = 1
    # for comment in c:
    #     f = open("commentConspiracy" + str(file_num) + ".json", "w")
    #     json.dump(requests.get("https://oauth.reddit.com/r/conspiracy/comments/" + comment, headers=headers,
    #     params={'limit': '100'}).json(), f)
    #     file_num += 1
    # f.close()

    # f = open("scrape1.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/politics/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # c = getCommentIDs("scrape1.json")
    # file_num = 1
    # for comment in c:
    #     f = open("commentPolitics" + str(file_num) + ".json", "w")
    #     json.dump(requests.get("https://oauth.reddit.com/r/politics/comments/" + comment, headers=headers,
    #     params={'limit': '100'}).json(), f)
    #     file_num += 1
    # f.close()

    # f = open("scrape2.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/TrueReddit/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # c = getCommentIDs("scrape2.json")
    # file_num = 1
    # for comment in c:
    #     f = open("commentTrueReddit" + str(file_num) + ".json", "w")
    #     json.dump(requests.get("https://oauth.reddit.com/r/TrueReddit/comments/" + comment, headers=headers,
    #     params={'limit': '100'}).json(), f)
    #     file_num += 1
    # f.close()

    # f = open("scrape3.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/PoliticalDiscussion/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # c = getCommentIDs("scrape3.json")
    # file_num = 1
    # for comment in c:
    #     f = open("commentPoliticalDiscussion" + str(file_num) + ".json", "w")
    #     json.dump(requests.get("https://oauth.reddit.com/r/PoliticalDiscussion/comments/" + comment, headers=headers,
    #     params={'limit': '100'}).json(), f)
    #     file_num += 1
    # f.close()

    # f = open("scrape4.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/changemyview/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # c = getCommentIDs("scrape4.json")
    # file_num = 1
    # for comment in c:
    #     f = open("commentChangeMyView" + str(file_num) + ".json", "w")
    #     json.dump(requests.get("https://oauth.reddit.com/r/changemyview/comments/" + comment, headers=headers,
    #     params={'limit': '100'}).json(), f)
    #     file_num += 1
    # f.close()

    # f = open("scrape5.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/Conservative/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # c = getCommentIDs("scrape5.json")
    # file_num = 1
    # for comment in c:
    #     f = open("commentConservative" + str(file_num) + ".json", "w")
    #     json.dump(requests.get("https://oauth.reddit.com/r/Conservative/comments/" + comment, headers=headers,
    #     params={'limit': '100'}).json(), f)
    #     file_num += 1
    # f.close()

    # f = open("scrape6.json", "w")
    # json.dump(requests.get("https://oauth.reddit.com/r/democrats/controversial", headers=headers,
    # params={'limit': '100'}).json(), f)
    # f.close()

    # c = getCommentIDs("scrape6.json")
    # file_num = 1
    # for comment in c:
    #     f = open("commentDemocrats" + str(file_num) + ".json", "w")
    #     json.dump(requests.get("https://oauth.reddit.com/r/democrats/comments/" + comment, headers=headers,
    #     params={'limit': '100'}).json(), f)
    #     file_num += 1
    # f.close()


if __name__ == '__main__':
    dataCollection()
