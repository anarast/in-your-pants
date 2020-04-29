import os
import requests
import json

from requests import Response
from random import randint

class TweetBuilder():
  num_results: int

  def __init__(self):
    self.num_results = 30
    self.base_volumes_url = 'https://www.googleapis.com/books/v1/volumes?q='
    self.in_your_pants = ' in your pants'
    self.language = 'en'
    self.print_type = 'books'
    self.fields = 'items(volumeInfo/title)'

  def build_tweet(self) -> str:
    return self.get_title() + self.in_your_pants

  def find_subject(self) -> str:
    with open('subjects.json', 'r') as read_file:
      data = json.load(read_file)

    nouns = data['nouns']
    genres = data['genres']

    noun_index = randint(0, len(nouns) - 1)
    genre_index = randint(0, len(genres) - 1)

    return nouns[noun_index] + genres[genre_index]

  def get_title(self) -> str:
    response = self.query_google_books()

    parsed_response = response.json()
    items = parsed_response['items']
    book_index = randint(0, self.num_results - 1)

    return items[book_index]['volumeInfo']['title']

  def query_google_books(self) -> Response:
    subject = self.find_subject()

    url = f"{self.base_volumes_url}{subject}&fields={self.fields}&printType={self.print_type}&maxResults={self.num_results}&langRestrict={self.language}"

    return requests.get(url=url)
