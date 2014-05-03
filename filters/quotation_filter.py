class QuotationFilter:
  def __init__(self, prevFilter):
    self.prevFilter = prevFilter
    self.prevText = prevFilter.getFilteredText()
  def getFilteredText(self):
    listPrevText = list(self.prevText)
    newListPrevText = []
    for char in listPrevText:
      if char is "'" or char is '"':
        continue
      newListPrevText.append(char)
    return ''.join(newListPrevText)

        
