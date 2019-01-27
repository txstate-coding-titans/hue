import praw

reddit = praw.Reddit(client_id= '' ,
	client_secret = '',
	username='TheHeartlessOne2121',
	password='',
	user_agent='SAVEapp')

subreddit = reddit.subreddit('SuicideWatch')


hot_python = subreddit.hot(limit = 5)

for submission in hot_python:
	print(submission.selftext)
