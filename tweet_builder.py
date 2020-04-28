import os
import requests
import json

from random import randint

class TweetBuilder():

  def build_tweet(self) -> str:
    return self.get_title() + " in your pants"

  def find_subject(self) -> str:
    with open("subjects.json", "r") as read_file:
      data = json.load(read_file)

    subjects = data['subjects']
    rand_num = randint(0, len(subjects) - 1)
    return subjects[rand_num]

  def get_title(self) -> str:
    subject = self.find_subject()
    url = f"https://www.googleapis.com/books/v1/volumes?q={subject}&fields=items(volumeInfo/title)"
    response = requests.get(url=url)
    parsed_response = response.json()
    items = parsed_response['items']
    return items[self.get_book_index()]['volumeInfo']['title']

  def get_book_index(self) -> int:
    return randint(0, 9)

