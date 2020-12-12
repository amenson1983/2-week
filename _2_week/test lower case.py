action = "" #Variable to start cycle
start_engine = "start"
stop_engine = "stop"
help = "help"
started = False
while True:
    action = input(">>> ").lower()
    if action == start_engine:
        if started == False:
            print("The engine has been started")
            started = True
        else: print("Started already")
    elif action == stop_engine:
        if started == True:
            print("The engine has been stopped")
            started = False
        else: print("Stopped already")
    elif action == help:
        print("""
start - starts
stop - stops""")
    elif action == "quit":
        break
else: print("I don`t understand, my friend")


