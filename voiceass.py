import webbrowser
import datetime
import sys

def respond(text):
    print("Assistant: ",text)


def handle_command(command):
    command = command.lower().strip()
    if command in ("hi", "hello", "Hey there!"):
        respond("Hello! How are you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        respond(f"Today's time is: {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%Y-%m-%d")
        respond(f"Today's date is: {today}")
    elif command.startswith("search"):
        q = command.replace("search", "").strip()
        if q:
            respond(f"Searching for:  {q}")
            webbrowser.open(f"https://www.google.com/search?q={q}")
        else:
            respond("Type somethingf else")
    elif command in ("exit", "quit", "bye"):
        respond("Good Bye!")
        sys.exit(0)
    else:
        respond("Sorry! I can't understand clearly!")
    

    def main():
        print("------Basic Voice Assistant(Text only)------")
        print("Type command like:" )
        print(" hello")
        print(" time")
        print(" date")
        print(" search")
        print(" exit")
        print("-----------------------------------------------")

        while True:
            user_input = input("You: ")
            handle_command(user_input)

    if __name__ == "__main__":
        main()