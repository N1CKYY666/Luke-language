import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import random

duration = 5
sample_rate = 44100
recognizer = sr.Recognizer()


def listenupbruh():
    print("\n🎧 Speak now...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    #OH MY GOD IS ALBERT EINSTEIN 
    sd.wait()
    wav.write("output.wav", sample_rate, recording)

    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text.lower()

    except:
        print("Bro... was that even English?")
        return ""


def level_1():
    print("\n------------------------")
    print("    Level 1 - Words!")
    print("------------------------")

    words = ["apple", "house", "coffee", "teacher", "chicken"]
    random.shuffle(words)

    score = 0

    for word in words[:3]:
        print("\nRepeat this word pliz:")
        print(">>", word)

        answer = listenupbruh()

        if answer == word:
            print("⭐ Correct!")
            score += 10
        else:
            print("😵‍💫 Wrong!")
            print("The answer is:", word)

    print("\nYour level 1 score:", score)

    return score


def level_2():
    print("\n------------------------")
    print("   Level 2 - Sentences")
    print("------------------------")

    sentences = [
        "good morning",
        "I like coffee",
        "I have a dog",
        "I am a student"
    ]

    random.shuffle(sentences)

    score = 0

    for sentence in sentences[:3]:
        print("\nRepeat this sentence :3:")
        print(">>", sentence)

        answer = listenupbruh()

        if answer == sentence.lower():
            print("⭐ Correct!")
            score += 20
        else:
            print("😵‍💫 Wrong!")
            print("The answer is:", sentence)

    print("\nYour level 2 score:", score)

    return score

def level_3():
    print("\n------------------------")
    print("   Level 3 - Translate")
    print("------------------------")

    words = {
        "casa": "house",
        "perro": "dog",
        "gato": "cat",
        "agua": "water",
        "escuela": "school"
    }

    questions = list(words.items())
    random.shuffle(questions)

    score = 0


    for spanish, english in questions[:3]:
        print("\nSay this word in English buddy:")
        print(">>", spanish)

        answer = listenupbruh()

        if answer == english:
            print("⭐ Correct!")
            score += 30
        else:
            print("😵‍💫 Wrong!")
            print("The answer is:", english)

    print("\nYour level 3 score:", score)

    return score

print("------------------------")
print("      English Game")
print("------------------------")

print("""
1. Level 1 - 🔤 Words?
2. Level 2 - 📖 Sentences?
3. Level 3 - 🌍 Translate?
4. Play all?
""")

option = input("Choose pliz: ")

total = 0

if option == "1":
    total = level_1()

elif option == "2":
    total = level_2()

elif option == "3":
    total = level_3()

elif option == "4":
    total += level_1()
    total += level_2()
    total += level_3()

else:
    print("Invalid option")

print("\n------------------------")
print(" 🏆 - Your final score:", total)
print("------------------------")

 
