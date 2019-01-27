# Usage: tone_azure.py [API key]
#demonstrates Microsoft Cognitive API calls
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
  {'id': '7', 'language': 'en', 'text': 'TELL ME YOU DON\'T LIKE ME I KNOW YOU ARE BETTER THEN ME!'},
  {'id': '8', 'language': 'en', 'text': 'Give up! Because there will come a day — trust me on this, there will come many days where I did kill myself.'}
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


# {'documents': [{'id': '1', 'score': 0.9708490371704102},
#                {'id': '2', 'score': 0.0019068121910095215},
#                {'id': '5', 'score': 0.7546495199203491},
#                {'id': '6', 'score': 0.7581720352172852},
#                {'id': '7', 'score': 0.0857938826084137},
#                {'id': '3', 'score': 0.7456425428390503},
#                {'id': '4', 'score': 0.334433376789093}],
#  'errors': []}
# {'documents': [{'id': '1',
#                 'keyPhrases': ['wonderful experience', 'staff', 'rooms']},
#                {'id': '2',
#                 'keyPhrases': ['food', 'terrible time', 'hotel', 'staff']},
#                {'id': '3', 'keyPhrases': ['Monte Rainier', 'caminos']},
#                {'id': '4', 'keyPhrases': ['carretera', 'tráfico', 'día']},
#                {'id': '5',
#                 'keyPhrases': ['best of friends',
#                                'years',
#                                'highschool',
#                                'months']},
#                {'id': '6', 'keyPhrases': ['best of friends']},
#                {'id': '7', 'keyPhrases': []}],
#  'errors': []}

