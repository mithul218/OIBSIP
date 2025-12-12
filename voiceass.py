import webbrowser
import datetime
import sys

def respond(txt):
    print("Assistant: ",txt)


def handle_command(cmd):
    cmd = cmd.lower().strip()
    if cmd in ("hi", "hello", "Hey there!"):
        respond("Hello! How are you?")
    elif "time" in cmd:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        respond(f"Today's time is: {now}")
    elif "date" in cmd:
        today = datetime.date.today().strftime("%Y-%m-%d")
        respond(f"Today's date is: {today}")
    elif cmd.startswith("search"):
        q = cmd.replace("search", "").strip()
        if q:
            respond(f"Searching for:  {q}")
            webbrowser.open(f"https://www.google.com/search?q={q}")
        else:
            respond("Type somethingf else")
    elif cmd in ("exit", "quit", "bye"):
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
