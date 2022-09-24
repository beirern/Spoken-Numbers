from google.cloud import texttospeech

import html

class TTSClient:
  def __init__(self):
    self.client = texttospeech.TextToSpeechClient()
    self.voice = texttospeech.VoiceSelectionParams(
      language_code="en-US",
      name="en-US-Wavenet-A",
      ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    )

    self.audio_config = texttospeech.AudioConfig(
      audio_encoding=texttospeech.AudioEncoding.MP3
    )

  def text_to_ssml(self, text_file):
    # Generates SSML text from plaintext.
    # Given an input filename, this function converts the contents of the text
    # file into a string of formatted SSML text. This function formats the SSML
    # string so that, when synthesized, the synthetic audio will pause for two
    # seconds between each line of the text file. This function also handles
    # special text characters which might interfere with SSML commands.
    #
    # Args:
    # inputfile: string name of plaintext file
    #
    # Returns:
    # A string of SSML text based on plaintext input

    # Parses lines of input file
    with open(text_file, "r") as f:
      raw_lines = f.read()

    # Replace special characters with HTML Ampersand Character Codes
    # These Codes prevent the API from confusing text with
    # SSML commands
    # For example, '<' --> '&lt;' and '&' --> '&amp;'

    escaped_lines = html.escape(raw_lines)

    # Convert plaintext to SSML
    # Wait two seconds between each combo
    ssml = "<speak>{}</speak>".format(
        escaped_lines.replace("\n", '\n<break time="2s"/>')
    )

    # Return the concatenated string of ssml script
    return ssml

  def get_mp3(self, text):
    ssml = self.text_to_ssml(text)
    input_text = texttospeech.SynthesisInput(text=ssml)
    response = self.client.synthesize_speech(
      request={"input": input_text, "voice": self.voice, "audio_config": self.audio_config}
    )

    print(input_text)

    with open("output.mp3", "wb") as out:
      out.write(response.audio_content)
      print('Audio content written to file "output.mp3"')
