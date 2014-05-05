from models.token_count import TokenCount
from parsers.stopwords_parser import StopWordsParser
from parsers.token_stemmer import TokenStemmer
from filters.text_filter import TextFilter
import nltk
import os
import redis
import heapq

ARTICLES_ROOT = 'test/articles/'
r = redis.StrictRedis(host="localhost", port=6379, db=0)

def main():
  
  test_articles = os.listdir(ARTICLES_ROOT)
  articlesDict = {}

  for article in test_articles:
    articlesDict[article] = ''
    article_path = ARTICLES_ROOT + article
    article_content = open(article_path)

    for line in article_content:
      articlesDict[article] = articlesDict[article] + line

  for article in articlesDict:
    stopWordsParser = StopWordsParser(open('resources/stopwords_formatted.1.txt'))
    withoutStopWords = stopWordsParser.removeStopWords(articlesDict[article])
    tokens = nltk.word_tokenize(withoutStopWords)
    #stemmedTokens = TokenStemmer(tokens).getStemmedTokens()
    #doing this totally the wrong way. have to do a word count first of the words in the thing
    countOfTokens = count(tokens)
    print countOfTokens
    #analyze(set(tokens))

def count(tokens):
  count = {}
  for token in tokens:
    if token in count:
      count[token] += 1
    else:
      count[token] = 1
  return count
def analyze(stemmedTokens):
  topHeap = []
  for token in stemmedTokens:
    value = r.get(token)
    if value is not None:
      tokenCount = TokenCount(token, int(value))
      print tokenCount

      if len(topHeap) < 50 :
        heapq.heappush(topHeap, tokenCount)

      elif topHeap[0] < tokenCount:
        heapq.heappushpop(topHeap, tokenCount)

  while len(topHeap) > 0:
    element = heapq.heappop(topHeap)
    print element


if __name__ == "__main__":
  main()
