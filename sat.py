import speech_recognition as spr
import pyttsx3

r = spr.Recognizer()

while(1):

    try:

        with spr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)

            myText = r.recognize_google(audio2)
            myText = myText.lower()

            print(myText)

    except spr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except spr.UnknownValueError:
        print("unknown error occured")
