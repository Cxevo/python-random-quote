import random
import sys

def main():
  sys.stdout.write("Quote Generator. ")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  f = open("quotes.txt", "a")
  f.write('The best is yet to be. \n')
  f.close()
  last = 19
  first = 1
  rnd = random.randint(1, last)
  rnd2 = random.randint(1, first)
  
  print(quotes[rnd], end='' )
  sys.stdout.write(quotes[rnd2])

if __name__== "__main__":
  main()
