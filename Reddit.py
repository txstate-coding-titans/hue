import praw

reddit = praw.Reddit(client_id= 'FiYE4ww3cnEQDQ' ,
	client_secret = 'Vk7Fwl9DJTHX7dCqsJpviK82H8E',
	username='TheHeartlessOne2121',
	password='Liveon21',
	user_agent='SAVEapp')

subreddit = reddit.subreddit('SuicideWatch')


hot_python = subreddit.hot(limit = 5)

for submission in hot_python:
	print(submission.selftext)