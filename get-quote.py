import random

def main():

  print('enter a quote. ')      
        
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  try:
      quote = input()
  except KeyboardInterrupt:
      print('CTRL+C exception. Please run again and input a quote!')
  else:
      f = open("quotes.txt", "a")
      f.write('\n' + quote)
      f.close()
  
  last = random.randint(1, 999)
  rnd = random.randint(1, last)
  rnd2 = random.randint(1, last)
  
  print(quotes[rnd2], end='')
  print(quotes[rnd], end='')
  
if __name__== "__main__":
  main()
