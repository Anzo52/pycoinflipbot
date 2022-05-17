from __future__ import print_function
import random
import schedule
import time
from random import randint, choice


score = 0
coin_flip = 0
coin_guess = 0
dt = time.ctime()
dtstr = str(dt)

def flip():
  for _ in range(1):
    k = random.randint(0, 1)
    coin_flip = k
    return coin_flip
    
def guess():
  for _ in range(1):
    k = random.randint(0,1)
    coin_guess = k
    return coin_guess
  
def scoring():
  if (abs(coin_flip - coin_guess)) > 0:
    score -= 1
  else:
    score += 1
  return score


def print_score():
    print(dtstr + " " + score)

schedule.every(1).minutes.do(flip)
schedule.every(1).minutes.do(guess)
schedule.every(1).minutes.do(print_score)
while True:
  schedule.run_pending()
  time.sleep(1)
