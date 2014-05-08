import socket
class PlingStemmer:
  def __init__(self, tokens, host = 'localhost', port=4444):
    self.tokens = tokens
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.connect((host, port))
    self.stopSym = self.s.recv(1000)

  def getStemmedTokens(self):
    stemmedTokens = []
    for word in self.tokens:
      stemmedTokens.append(self.stem(word))

    self.s.send(self.stopSym) #send token to tell server to stop
    return stemmedTokens

  def stem(self, word):   
    self.s.send(word.strip() + '\n')  
    data = self.s.recv(10000)
    print data[:-1]
    return data[:-1] 

