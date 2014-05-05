from nltk import PorterStemmer
class TokenStemmer:
  def __init__(self, tokens):
    self.tokens = tokens

  def getStemmedTokens(self):
    stemmer = PorterStemmer()
    stemmedTokens = []
    for word in self.tokens:
      stemmedTokens.append(stemmer.stem(word))
    return stemmedTokens
