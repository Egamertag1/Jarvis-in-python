from gtts import gTTS #pip install gtts
import pygame #pip install pygame
import os #pip install os
import tempfile #pip install tempfile 
import openai #pip install openai
import speech_recognition as sr #pip install speech_recognition
import pyttsx3 #pip install pyttsx3


print('running')
# Set your OpenAI API key here
api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

# Check if the variable contains a certain word
word_to_check = "jarvis"
word_to_check2 = "Jarvis"

def chat_with_gpt(prompt):
    try:
        # You can adjust the parameters according to your needs
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            n = 1
        )

        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

r = sr.Recognizer()

# creates the main function
def record_text():
    # creates the while loop
    while(1):
        try:
            #checks if you have a microphone is in headphone jack 2
            with sr.Microphone() as source2:
                # adjusts for background noise
                r.adjust_for_ambient_noise(source2,duration=0.2)
                # listons for audio
                audio2 = r.listen(source2)
                # uses google
                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("it hates you")
        

    return
# creates the function that starts writing it
def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

# records your words

def text_to_speech_and_play(text, output_file):
    try:
        # Convert text to speech and save it to the specified output file
        tts = gTTS(text, lang="en")
        tts.save(output_file)

        # Initialize Pygame and play the audio
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(2)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up Pygame resources (you can remove this block if you want to keep the file)
        pygame.mixer.quit()
        pygame.quit()

def delete_file_by_name(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred while deleting '{file_name}': {e}")

def JARVIS():

    while(1):
        # calling the funbction
        text = record_text()
        output_text(text)
        # checking if it contains the word jarvis
        if word_to_check in text or word_to_check2 in text:
            if __name__ == "__main__":
                user_input =(text)
                if user_input.lower() in ["exit", "quit"]:
                    break
                response = chat_with_gpt(user_input)
            if __name__ == "__main__":
                text_to_convert = response  # Replace with your text
                output_audio_file = "output_audio.mp3"  # Specify the name of the output audio file
    
                # Call the function to convert text to speech and save it to the specified output file
                text_to_speech_and_play(text_to_convert, output_audio_file)

                if __name__ == "__main__":
                    file_to_delete = "output_audio.mp3"  # Specify the name of the file you want to delete
                    delete_file_by_name(file_to_delete)
            JARVIS()
        else:
            print(f"The variable does not contain the word '{word_to_check}'.")
            JARVIS()
        # prints the output
        print(text)


JARVIS()