from google.cloud import language 
from google.cloud.language import enums 
from google.cloud.language import types
import praw

client = language.LanguageServiceClient()

reddit = praw.Reddit(client_id= 'FiYE4ww3cnEQDQ' ,
	client_secret = 'Vk7Fwl9DJTHX7dCqsJpviK82H8E',
	username='TheHeartlessOne2121',
	password='Liveon21',
	user_agent='SAVEapp')

subreddit = reddit.subreddit('SuicideWatch')

hot_python = subreddit.hot(limit = 10)

for submissions in hot_python:
	text = submissions.selftext
	document = types.Document(
		content = text,
		type=enums.Document.Type.PLAIN_TEXT)
	sentiment = client.analyze_sentiment(document = document).document_sentiment
	#print('Text:{}'.format(text.encode('utf-8')))
	print('Sentiment: {},{}'.format(sentiment.score,sentiment.magnitude))

