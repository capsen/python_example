import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
   engine.say('你好，你知道我是谁吗？')
engine.runAndWait()