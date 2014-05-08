from pling_stemmer import PlingStemmer
import socket
from nltk import PorterStemmer

class TokenStemmer:
  def __init__(self, tokens):
    self.tokens = tokens

  def getStemmedTokens(self):
    stemmer = PlingStemmer(self.tokens)
    return stemmer.getStemmedTokens()
