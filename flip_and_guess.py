from __future__ import print_function
import random
import schedule
import time

global score1
score1 = 0

dt = time.ctime()

def guess():
  guess = random.randint(0, 1)
  return guess

def flip():
  flip = random.randint(0, 1)
  return flip

def everything():
  global score1
  
  guess1 = guess()
  flip1 = flip()
  if flip1 == guess1:
    score1 = score1 + 1
  else:
    score1 = score1 - 1
  print(f"{dt}, Score: {score1},")



schedule.every(0.01).minutes.do(everything)


while True:
  schedule.run_pending()
  time.sleep(1)
