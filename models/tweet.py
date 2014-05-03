
class Tweet:
  def __init__(self, raw_tweet):
    self.raw_tweet = raw_tweet
    parse(raw_tweet)

  def parse(self, raw_tweet):
    print raw_tweet

