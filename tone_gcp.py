# Imports the Google Cloud client library
import os
import sys
import argparse
import io
import json

from google.cloud import language
import six

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=sys.argv[1] #import credentials

def classify(text, verbose=True):
    """Classify the input text into categories. """

    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category.name))
            print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result

if __name__ == '__main__':
    classify("All of this negatively effected my relationship with my gf a tiny bit, but me and her had our own problems. She was someone who also had a lot of walls, had trouble being honest, and hated any kind of conflict, even when it was necessary. she hated being uncomfortable emotionally, and spent the first 4 years of our relationship being very emotionally manipulative, she even admitted to it later before she got a bit better at treating people as they should be. I cant get into our entire relationship. This story is already long enough. It is enough to say that I loved and love her dearly, so much it hurts, despite our problems. She has not talked to me once since the day she left.")