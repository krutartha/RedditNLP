# RedditNLP
Found at https://github.com/krutartha/RedditNLP

## Setup and Running instructions
```
pip install -r requirements.txt
python main.py
```

The main.py files runs the following functions in the given order:

1. Collecting comment IDs from general scrape files
2. Creating subreddit files for comments based on subreddit
3. Scrape comment for each subreddit file from the respective subreddit comment ID file
4. Basic Sentiment Analysis
5. Create Sentiment Change Over Time graphs
6. Extract keywords and combining keywords and combining sentiment analysis
7. Create Histogram for combined Analysis
8. Sort subreddit data based on sentiment sorting
9. Extracting keywords from comment scrapes
10. Extacting keywords from POST scrapes
11. Computing the average sentiment scores
12. Create Word Clouds
13. Create Pie Charts

**Note**: Ensure you have set the necessary variables in your local ***.env*** file!
**Note**: We have alredy attached the general data scrape files in order to save time and API requests for the tester!




**Note**: main.py may have to be run in batches (by commenting out code) to ensure that the Reddit API requests do not exceed the allowed amount. 

## Project Idea

Our project is focused on investigating possible echo chambers created within subreddits on Reddit.com. The forum-based social media platform allows users to create niche subreddits for any possible topic or community. Given this freedom, many subreddits favor both sides of the political spectrum. Using existing political and controversial subreddits such as:
* r/Conspiracy
* r/politics
* r/PoliticalDiscussion
* r/truereddit
* r/changemyview
* r/conservative 
* r/democrats

We hope to investigate these subreddits to try and find any relationship between users and an "echo-chamber" environment. Although this idea of echo chambers is rather vague, we hope to quantify this by using data mining techniques to gauge whether comments generally agree or disagree with the content or ideas presented within the post. 

Throughout our project, we plan on using text categorization to segment topics and issues that are talked about frequently on each subreddit. In addition, we plan on using sentiment analysis to determine the tone of each post made on said topic. Given this analysis, we will process the set of comments made under each post, and determine whether the comment is either in favor of the issue or stance made in the post.

## Features

Our project showcases various processes and features that will help achieve its objectives:

* **Data Collection** - This feature relates to setting up a developer account on the Reddit API Dashboard and making https requests to the endpoints exposed by the API to collect desired data. As part of data collection, there will also be various filtering techniques used to gather subreddit specific data, along with other filters like keywords, time period, etc. 

* **Data Preprocessing** - This process will involve the cleaning up and processing of the data we gather from the Reddit API. Ensuring the data gathered is in a usable format and dealing with missing values, duplicates, and irrelevant data are also features of this process.  Textual processing methods like tokenization, stemming, and lemmatization will also be followed in this stage. 

* **Sentiment Analysis** - Following the preprocessing methods, the project will then feature a textual sentiment analysis of the processed data. This involves converting processed data into numerical features that can be fed into machine learning algorithms to get useful metrics like Bag-of-Words, and Term Frequency-Inverse Document Frequency (TF-IDF) etc. Then, using useful python libraries like nltk, we intend to classify each subreddit’s tone into the positive, negative, and neutral categories. 

* **General Trend Detection** - Using techniques like clustering, and token frequency detection, we intend to recognize the general consensus of the topics we analyze. If possible, we also intend to observe how the general consensus has shifted on topics over time. Additionally, we intend to do trend detection on the same topics but on different subreddits to examine the level of objectivity maintained by the subreddit’s users. 

All these features will be implemented while maintaining strict ethical considerations which involve ensuring privacy and confidentiality of user data and being compliant with the data usage policies of the Reddit API.  

## Significance

Our data mining project delves into the intersection of conceptual inquiry and technological application, combining personal passions and interests and fundamental skills learned in the course. 

Conceptually, our project tackles real-world issues, particularly amidst the current discourse surrounding the growing division within the United States. We aim to explore the motivations behind individuals in these divisive subreddits: whether to challenge their own perspectives, engage in close-minded debates, or simply find comfort in reaffirming beliefs. While each of these motivations likely plays a role to some degree, our project seeks to quantify the frequency of each action, providing valuable insights into societal dynamics, especially during this pivotal election year in 2024. 

Content-wise, our project utilizes skills learned in lecture and additionally requires us to learn skills outside of course focus. For example, Twitter (now X) is the focus of much of the lecture content. By focusing on Reddit, we must use the Twitter API knowledge we have built as a basis on how to use the Reddit API. Our project is largely sentiment analysis, and by building this project, we will be able to apply course concepts.

By completing this project, we hope for not only personal growth but also the potential to contribute meaningful insights to the broader discourse surrounding societal polarization and information consumption in the digital age. 


## To generate graphs:

- Run main.py with the correct credentials for CLIENT_ID, USERNAME, PASSWORD
- Install required nltk modules
- Run combined_SAKA.py file

## To get Sentiment Averages + Post/Comment Keywords
- Before running any files, the "comment_scrapes" directory must exist!
Instructions: 
- First, run combined_SAKA.py
- second, run postPartitioning.py
- third, run global_averageSentiment.py
The results are in the .txt files generated by global_averageSentiment.py.

## Work Plan

Week 1: Planning and Data Gathering
- Task 1: Project Kickoff Meeting
  - Description: Discuss project goals, assign roles, and establish communication channels.
  - Responsible: Team (All members)
  - Start/End Date: Mar 27, 2024
 
- Task 2: Data Gathering (Reddit API)
  - Description: Collect raw data from Reddit using the API.
  - Responsible: Ashley
  - Start Date: Mar 28, 2024
  - End Date: Apr 3, 2024

Week 2: Data Preprocessing and Initial Analysis
- Task 3: Data Preprocessing
  - Description: Clean and prepare the raw data for analysis.
  - Responsible: Adya
  - Start Date: Apr 3, 2024
  - End Date: Apr 7, 2024

- Task 4: Initial Sentiment Analysis
  - Description: Conduct basic sentiment analysis on preprocessed data.
  - Responsible: Krutartha
  - Start Date: Apr 7, 2024
  - End Date: Apr 10, 2024

Week 3: Advanced Analysis and Consensus Building
- Task 5: Advanced Sentiment Analysis
  - Description: Implement advanced sentiment analysis techniques for deeper insights.
  - Responsible: Krutartha with help from others
  - Start Date: Apr 10, 2024
  - End Date: Apr 15, 2024

- Task 6: General Consensus (Trend Detection)
  - Description: Identify trends and patterns in user sentiments to detect echo chambers.
  - Responsible: Anthony
  - Start Date: Apr 15, 2024
  - End Date: Apr 20, 2024

Week 4: Final Analysis and Report Preparation
- Task 7: Final Sentiment Analysis and Results
  - Description: Compile the results of sentiment analysis and consensus building.
  - Responsible: All members (Review and collaboration)
  - Start Date: Apr 20, 2024
  - End Date: Apr 23, 2024

- Task 8: Report Writing and Presentation
  - Description: Prepare the final project report and presentation.
  - Responsible: Team (All members contribute their parts)
  - Start Date: Apr 23, 2024
  - End Date: Apr 25, 2024

- Task 9: Final Review and Submission
  - Description: Review the report, make necessary revisions, and submit the project code.
  - Responsible: Team (All members)
  - Start Date: Apr 25, 2024
  - End Date: May 4, 2024




