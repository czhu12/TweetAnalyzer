class TweetFilter:
  def __init__(self, textFilter):
    self.textFilter = textFilter

    self.filteredWordArray = textFilter.getFilteredText().split()
    #print(self.filteredWordArray)
    if(self.isRetweet(self.filteredWordArray)):
      raise Exception

  def isRetweet(self, wordArray):
    return wordArray[0] == 'RT'

  def getFilteredText(self, params=[]):
    returnString = []
    for word in self.filteredWordArray:
      if(word[0] not in params):
        returnString.append(word)
    return ' '.join(returnString)

