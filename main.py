import math
import random as rand
import time

HIGHEST_COMBINATION = list(range(1, 5)) # Number of punches to react to
PUNCHES = list(range(1,7)) # Punching numbers, 1-6
BREAK = list(range(1,6)) # Seconds between combinations

# Returns a random number from a given list
def get_random_number(list_of_numbers):
  return list_of_numbers[math.floor(rand.random() * len(list_of_numbers))]

if __name__ == "__main__":
  while True:
    punches = []
    time.sleep(get_random_number(BREAK))
    for _ in range(0, get_random_number(HIGHEST_COMBINATION)):
      punches.append(get_random_number(PUNCHES))

    print(punches)
