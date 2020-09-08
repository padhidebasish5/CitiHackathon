Credit scoring using social media analytics.

Here we use social media analytics data and the customer personal information to predict whether the customer who has applied for loan is a potential candidate to return it or might come in the defaulter list.

Data Preparation:

So here we basically use the twitter information and the network information of the customer to actually figure out their personaility and based on the information.
These are the features being used in our model:
Age 21–50yrs
Gender -{male, female}
Marriage -{married, unmarried, divorced}
Children -{have, don’t have}
Family -{Number of family members the borrower has: 1, 2, 3, 4, 5}
Education -{Junior high school, masters, bachelors}
Income - The annual income of the borrower
Car -{yes, no}
Income_type -Income type, six types
House -{own, parent’s house, rent}
Work_days 3-7days
Registration_time -Numbers of minutes before the application the borrower started registration in this platform
Document_change -Numbers of minutes before the application the borrower changed his/her document
Jobtitle -Job title, six types
Amount -Loan amount
Rate -Loan rate
Period -8–45 months
Time -When the borrower applies for a loan during the day
Social_stability {1, 1–3 years, >3 years}
Social_exposure {1, 2, 3, 4}
Social_quality {0, 1, 2 or above}
Sentiment {0-neutral,1-positive}

Here we have not only included the traditional credit information but also the social parameters which we use to make the final prediction.

Steps to execute the solution:
Here since we have not deployed the code so,i would be showing manual way to execute the code and reach the final output

1) Data preparation & Exploratory Data Analysis
 the first thing is to get the customer's twitter information since this is the part we are majorly using for all the social information and it will also help us to get an insight to how that person's personality would be
We use Twitter API in order to fetch the tweets based on some hashtags which would be related to his lifestyle personality etc

i)Go to the tweepy crawler folder
ii)open tweepy1.py file >download it or copy it to the local IDE
iii)Replace the API keys and the search path in order to fetch tweets
iv)once the tweets appear in the console, copy them to a csv file
v) perform some preprocessing to make it structured as this would be used as input in the next step.

SENTIMENT ANALYSIS & OTHER SOCIAL PARAMETERS
After we receive the tweets in the csv format we actually divide the tweets into train and test tweets as we need to find the sentiment analysis on the basis of that, we also take 
these tweets and try to analyze them in order to find few other social parameters which are social network quality, social exposure & social stability

i)Go to the sentiment analysis folder
ii)place the structured tweets which we fetched in the previous steps, i.e the train and test tweets in the path where we need to run the file
iii)
