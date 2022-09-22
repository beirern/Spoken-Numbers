from google.cloud import texttospeech

import playsound
import math
import random as rand
import time

NUMBER_OF_COMBINATIONS = 3 # Number of combinations before exiting
HIGHEST_COMBINATION = list(range(1, 5)) # Number of punches to react to
PUNCHES = list(range(1,7)) # Punching numbers, 1-6
# TODO: MAKE THIS A FLOAT
BREAK = list(range(1,3)) # Seconds between combinations

# Returns a random number from a given list
def get_random_number(list_of_numbers):
  return list_of_numbers[math.floor(rand.random() * len(list_of_numbers))]

if __name__ == "__main__":
  client = texttospeech.TextToSpeechClient()

  for _ in range(0, NUMBER_OF_COMBINATIONS):
    punches = ""
    time.sleep(get_random_number(BREAK))
    for _ in range(0, get_random_number(HIGHEST_COMBINATION)):
      punches += str(get_random_number(PUNCHES)) + ","
    punches = punches[:-1] # Remove extra comma at end

    print(punches)

    # TODO: MAKE GOOGLE ITS OWN MODULE OR METHOD
    input_text = texttospeech.SynthesisInput(text=punches)
    # TODO: CHANGE THIS VOICE PLEASE
    voice = texttospeech.VoiceSelectionParams(
      language_code="en-US",
      name="en-US-Standard-C",
      ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
      audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
      request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    with open("output.mp3", "wb") as out:
      out.write(response.audio_content)
      print('Audio content written to file "output.mp3"')

    playsound.playsound("output.mp3")
