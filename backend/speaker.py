import boto3
import os

from typing import List
from dotenv import load_dotenv

class Speaker:
    def __init__(self) -> None:
        load_dotenv()
        self.client = boto3.client('polly', 
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"], 
            region_name='us-east-1'
        )

    def text_to_ssml(self, punches: List[str], pauses: List[int]) -> str:
        ssml_text = ""
        for count, combo in enumerate(punches):
            if count != len(punches) - 1:
                ssml_text += '<say-as interpret-as="digits">{}</say-as><break time="{}s"/>'.format(
                    combo,
                    pauses[count]
                )
            else:
                ssml_text += '<say-as interpret-as="digits">{}</say-as>'.format(combo)
        return "<speak>{}</speak>".format(ssml_text)

    def speak(self, punches: List[str], pauses: List[int]) -> str:
        ssml_text = self.text_to_ssml(punches, pauses)
        response = self.client.start_speech_synthesis_task(
            Engine='standard',
            LanguageCode='en-US',
            OutputFormat='mp3',
            OutputS3BucketName='speaking-website',
            Text=ssml_text,
            TextType='ssml',
            VoiceId='Joey'
        )

        last_index = response['SynthesisTask']['OutputUri'].rindex('/')
        object_key = response['SynthesisTask']['OutputUri'][last_index:]
        print(object_key)
        # self.client.generate_presigned_url(
        #     ClientMethod='get_object',
        #     Params={
        #         'Bucket':'speaking-website',
        #         'Key': response['Key']
        #     },
        #     ExpiresIn=3600
        # )

        return response['SynthesisTask']['OutputUri']