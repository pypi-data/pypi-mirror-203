import subprocess
import threading
import time
import re
import os
import openai
import pyttsx3

def speak(text):
    # initialize the text-to-speech engine
    engine = pyttsx3.init()

    # set the rate and volume of the voice
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # ask the user for input
    # word = input(ticker)

    # speak the word
    engine.say(text)
    engine.runAndWait()

def chat(conversation,option):
    if len(conversation)>4096:
        prompt = conversation[-4096:]
    else:
        prompt = conversation
        
    if option=="explain":
        prompt=prompt+"\n explain above output."
    elif option=="suggest":
        prompt=prompt+"\n give debugging suggestions for above output."
    elif option=="chat":
        prompt==prompt
    elif option=="ask":
        prompt==prompt

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a Windows debugger copilot."},
            {"role": "user", "content": "How to start debugging a memory dump?"},
            {"role": "assistant", "content": "You may run !analyze -v"},
            {"role": "user", "content": prompt}
        ]
    )
    # response=openai.Completion.create(
    # model="gpt-3.5-turbo",
    # prompt=output,
    # max_tokens=4096,
    # temperature=0
    # )
    text = response.choices[0].message.content.strip()
    print("\n"+text)
    return text

class ReaderThread(threading.Thread):
    def __init__(self, stream):
        super().__init__()
        self.buffer_lock = threading.Lock()
        self.stream = stream  # underlying stream for reading
        self.output = ""  # holds console output which can be retrieved by getoutput()

    def run(self):
        """
        Reads one from the stream line by lines and caches the result.
        :return: when the underlying stream was closed.
        """
        while True:
            line = self.stream.readline()  # readline() will block and wait for \r\n
            if len(line) == 0:  # this will only apply if the stream was closed. Otherwise there is always \r\n
                break
            with self.buffer_lock:
                self.output += line

    def getoutput(self, timeout=0.1):
        """
        Get the console output that has been cached until now.
        If there's still output incoming, it will continue waiting in 1/10 of a second until no new
        output has been detected.
        :return:
        """
        temp = ""
        while True:
            time.sleep(timeout)
            if self.output == temp:
                break  # no new output for 100 ms, assume it's complete
            else:
                temp = self.output
        with self.buffer_lock:
            temp = self.output
            self.output = ""
        return temp

print("Hello engineer, I am Windows debugger copilot, I'm here to assist you.")
speak("Hello engineer, I am Windows debugger copilot, I'm here to assist you.")

print("\nThis software is used for Windows debugging learning purpose, do NOT load any customer data, all input and output will be sent to OpenAI API.")
speak("This software is used for Windows debugging learning purpose, do NOT load any customer data, all input and output will be sent to OpenAI API.")

print("\nFirst, Where is the memory dump?")
speak("First, Where is the memory dump?")

filename = input("Memory dump file location:")

while not os.path.exists(filename):
    print("\nFile does not exist")
    speak("File does not exist")
    filename = input("Memory dump file location:")
    
command = r'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe'
arguments = [command]
arguments.extend(['-y', "srv*C:\debug\symbols*https://msdl.microsoft.com/download/symbols"])  # Symbol path, may use sys.argv[1]
# arguments.extend(['-i', sys.argv[2]])  # Image path
arguments.extend(['-z', filename])  # Dump file
arguments.extend(['-c', ".echo LOADING DONE"])
process = subprocess.Popen(arguments, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
reader = ReaderThread(process.stdout)
reader.start()

result = ""
while not re.search("LOADING DONE", result):
    result = reader.getoutput()  # ignore initial output

def dbg(command):
    process.stdin.write(command+"\r\n")
    process.stdin.flush()
    result = ""
    while result == "":
        result = reader.getoutput(timeout=2)
    return result

dump_type = ""

result = dbg("||")
print(result)
speak(result)
if "user mini" in result:
    dump_type="User"
    print("Yay, it's a User mode dump")
    speak("Yay, it's a User mode dump")
elif "kernel" in result:
    dump_type="Kernel"
    print("Yay, it's a Kernel mode dump")
    speak("Yay, it's a Kernel mode dump")
    
# result = dbg("!analyze -v")
# print(result)
# chat(result,"explain")
# chat(result,"suggest")

conversation=""
while True:
    # Prompt the user for input
    
    speak("I am your Windows debugger copilot, please enter your input.")
    user_input = input("\n"+'kd> ')
    
    speak("your input is "+user_input)
    if user_input.startswith("!chat"):
        text=chat(user_input,"chat")
        speak(text)
    elif user_input.startswith("!explain"):
        # Print the output of cdb.exe
        text=chat(conversation,"explain")
        speak(text)
    elif user_input.startswith("!suggest"):
        # Print the output of cdb.exe
        text=chat(conversation,"suggest")
        speak(text)
    elif user_input.startswith("!ask"):
        # Print the output of cdb.exe
        question = conversation + "\n" + user_input[4:]
        text=chat(question,"ask")
        speak(text)
    elif user_input.startswith("!q"):
        # Print the output of cdb.exe
        text=chat("Goodbye Windows debugger copilot, please quit","chat")
        speak(text)
        dbg("q")
        break
    elif user_input.startswith("!help"):
        help_msg = '''
        !chat <you may ask anything related to debugging>
        !ask <ask any question for the above output>
        !explain: explain the last output
        !suggest: suggest how to do next
        !q: quit
        '''
        print(help_msg)
        speak(help_msg)
    else:
        # Send the user input to cdb.exe
        result = dbg(user_input)
        conversation += "\n"+result
        print("\n"+result)



