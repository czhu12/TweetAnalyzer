import json
import re

class TextFilter:
  def __init__(self, raw_tweet):
    jsonTweet = json.loads(raw_tweet)
    if 'delete' in jsonTweet:
      self.filtered_text = None
      return
    text = jsonTweet['text']
    self.filtered_text = text
    #self.filtered_text = re.findall("\w+", text)

  def getFilteredText(self):
    if(self.filtered_text is None):
      raise Exception('deleted tweet')
    return self.filtered_text
