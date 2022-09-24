import math
import random as rand
from flask import jsonify

from speaker import Speaker
from s3 import S3

PUNCHES = list(range(1,7)) # Punching numbers, 1-6
# TODO: MAKE THIS A FLOAT
BREAK = list(range(1,3)) # Seconds between combinations

# Returns a random number from a given list
def get_random_number(list_of_numbers):
  return list_of_numbers[math.floor(rand.random() * len(list_of_numbers))]

def boxing_combination(num_punches: int, num_rounds: int) -> None:
  speaker = Speaker()
  # Makes a list for getting random numbers to work
  # TODO: MORE VALIDITY CHECKING (EXPECTING IT TO BE >= 1)
  num_punches = list(range(1, num_punches + 1))

  punches = []
  pause_times = []
  for _ in range(0, num_rounds):
    pause_times.append(get_random_number(BREAK))
    combo = ""
    for _ in range(0, get_random_number(num_punches)):
      combo += str(get_random_number(PUNCHES))
    punches.append(combo)

  pause_times.pop()  
  s3_uri = speaker.generate_mp3(punches, pause_times)
  
  s3 = S3()
  presigned_url = s3.get_presigned_url(s3_uri, 'speaking-website')

  response = jsonify({'presigned_url': presigned_url})
  
  return response

  
