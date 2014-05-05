from twitter.twitter_bridge import TwitterBridge
from filters.text_filter import TextFilter
from filters.tweet_filter import TweetFilter
from filters.quotation_filter import QuotationFilter
from parsers.tweet_parser import TweetParser
from redis_wrapper.redis_bridge import RedisBridge
from parsers.token_stemmer import TokenStemmer

import json
import nltk
import re

if __name__ == "__main__":
  redisBridge = RedisBridge()
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
    afterStopWords = parser.removeStopWords(textFiltered)
    tokens = nltk.word_tokenize(afterStopWords)
    #stemmedTokens = TokenStemmer(tokens).getStemmedTokens()
    redisBridge.addAll(stemmedTokens)
    

  bridge.subscribe(callback)
  bridge.fetchStream()
