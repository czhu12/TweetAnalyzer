import json
import re

class TextFilter:
  def __init__(self, raw_tweet):
    jsonTweet = json.loads(raw_tweet)
    if 'delete' in jsonTweet or jsonTweet['lang'].encode('utf-8') != u'en':
      self.filtered_text = None
      return

    #print jsonTweet['lang']

    text = jsonTweet['text']
    self.filtered_text = text.encode()
    #self.filtered_text = re.findall("\w+", text)

  def getFilteredText(self):
    if(self.filtered_text is None):
      raise Exception('deleted tweet')
    return self.filtered_text
