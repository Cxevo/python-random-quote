import random
import sys

def main():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  f = open("quotes.txt", "a")
  f.write('\n The best is yet to be. ')
  f.close()
  
  first = 1
  last = 19
  rnd = random.randint(1, last)
  rnd2 = random.randint(1, first)
  
  sys.stdout.write(quotes[rnd2])
  sys.stdout.write(quotes[rnd])
  
if __name__== "__main__":
  main()
