import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="92cca979db17452f8db5c7614bab3494", region="centralus")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

def speechtotext():
    audio_input = speechsdk.AudioConfig(filename='temp_audio.wav')
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    result = speech_recognizer.recognize_once_async().get()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
       return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized"

def texttospeech(text):  
    speech_config.speech_synthesis_voice_name='en-US-AriaNeural'
    audio_config = speechsdk.audio.AudioOutputConfig(filename="temp_audio_azure1.wav")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text)
    speech_config.speech_synthesis_voice_name='en-US-AnaNeural'
    audio_config = speechsdk.audio.AudioOutputConfig(filename="temp_audio_azure2.wav")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text)  
    speech_config.speech_synthesis_voice_name='en-US-EricNeural'   
    audio_config = speechsdk.audio.AudioOutputConfig(filename="temp_audio_azure3.wav")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text) 



