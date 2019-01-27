#To continue with this walkthrough, replace subscription_key with a valid subscription key that you obtained earlier.

import sys

subscription_key = sys.argv[1]
assert subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"

sentiment_api_url = text_analytics_base_url + "sentiment"
key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)
print(sentiment_api_url)

documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'},
  {'id': '5', 'language': 'en', 'text': 'In highschool? Where I was not the best of friends? That was nine years ago now. We had not seen each other since we graduated, and started hanging out again 30 months ago or so.'},
  {'id': '6', 'language': 'en', 'text': 'Where I was not the best of friends?'},
  {'id': '7', 'language': 'en', 'text': 'TELL ME YOU DON\'T LIKE ME I KNOW YOU ARE BETTER THEN ME!'}
]}

import requests
from pprint import pprint
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)

response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)
