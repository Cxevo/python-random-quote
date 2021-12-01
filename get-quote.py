import random

def main():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  f = open("quotes.txt", "a")
  quote = input("enter a quote: ")
  f.write('\n' + quote)
  f.close()
  
  first = 1
  last = 19
  rnd = random.randint(1, last)
  rnd2 = random.randint(1, first)
  
  print(quotes[rnd2], end='')
  print(quotes[rnd], end='')
  
if __name__== "__main__":
  main()
