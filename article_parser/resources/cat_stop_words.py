def main():
  words1 = open('stopwords.1.txt')
  for line in words1:
    if(len(line) > 1):
      print line[0:-1]

if __name__ == "__main__":
  main()
