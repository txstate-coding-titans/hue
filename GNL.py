from google.cloud import language 
from google.cloud.language import enums 
from google.cloud.language import types

client = language.LanguageServiceClient()

text = u'Hello this is the world. Welcome to it'

document = types.Document(
	content = text,
	type=enums.Document.Type.PLAIN_TEXT)

sentiment = client.analyze_sentiment(document = document).document_sentiment

print('Text:{}'.format(text))
print('Sentiment: {},{}'.format(sentiment.score,sentiment.magnitude))
