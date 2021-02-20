import os
chuck =0
while chuck<100:
    talk=input("What should I say:")
    os.environ['Google_Application_Credentials'] = 'XXXWHERE YOU PLACED YOUR JSON FILE WITH CREDENTIALSXXX'
    tts_client = texttospeech_v1.TextToSpeechClient()
    params = texttospeech_v1.VoiceSelectionParams(language_code='en-IN', name="en-IN-Wavenet-D")
    audio = texttospeech_v1.AudioConfig(audio_encoding = texttospeech_v1.AudioEncoding.MP3)
    si = texttospeech_v1.SynthesisInput(text=talk)
    response = tts_client.synthesize_speech(input=si, voice=params, audio_config=audio)
    f = open('says.mp3', 'wb')
    f.write(response.audio_content)
    f.close()
    os.system("WHATEVERYOUWANT.mp3")
    chuck=chuck+1
