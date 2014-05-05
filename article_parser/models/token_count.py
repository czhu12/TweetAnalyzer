class TokenCount:
  def __init__(self, key, value):
    self.key = key
    self.value = value
  def __cmp__(self, other):
    return cmp(self.value, other.value)
  def __str__(self):
    return self.key + " : " + str(self.value)
