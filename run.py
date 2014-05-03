from twitter.twitter_bridge import TwitterBridge
from filters.text_filter import TextFilter
from filters.tweet_filter import TweetFilter
from filters.quotation_filter import QuotationFilter
from parsers.tweet_parser import TweetParser

import json
import re

if __name__ == "__main__":
  bridge = TwitterBridge()
  def callback(raw_tweet):
    textFiltered = ''
    try: 
      #textFiltered = TextFilter(raw_tweet).getFilteredText()
      textFiltered = TweetFilter(QuotationFilter(TextFilter(raw_tweet))).getFilteredText(['@', '#'])

    except Exception:
      return

    #print textFiltered
    parser = TweetParser(open('resources/stopwords_formatted.1.txt'))
    print parser.removeStopWords(textFiltered)


  bridge.subscribe(callback)
  bridge.fetchStream()
