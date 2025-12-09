import webbrowser
import datetime
import sys

def respond(text):
    print("Assistant: ", text)

def handle_command(command):
    command = command.lower().strip()

    if command in ("hi", "hello", "hey"):
        respond("Hello! How are you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        respond(f"Now the  time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%Y-%m-%d")
        respond(f"Today's date is {today}")
    elif command.startswith("search"):
        query = command[len("search "):].strip()
        if query:
            respond(f"Open the browser for: {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            respond("Type something else with 'search'.")
    elif command in ("exit", "bye", "quit"):
        respond("Okay! Good Bye! Have a nice day!")
        sys.exit(0)
    else:
        respond("Sorry! I didn't understand!")

def main():
    print("---------Basic Voice Assistant (text only)---------")
    print("Type something: ")
    print(" hello")
    print(" date")
    print(" time")
    print(" search python programming")
    print(" exit")
    print("-----------------------------------------------------")
    
    while True:
        user_input = input("You: ")
        handle_command(user_input)


if __name__ == "__main__":
    main()
    

