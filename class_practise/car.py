if __name__ == '__main__':
    enter = input(">")
    counter = 0

    while counter <= 5:
        if enter == "help" or "Help":
            print("start\nStop\nQuit")
        else:
            print("i dont understand")

        enter1 = input(">")

        if enter1 == "start" or "Start":
            print("ready to start")
        else:
            print("i dont understand that")

        enter2 = input(">")

        if enter2 == "Stop" or "stop":
            print("Car stopped")
        else:
            print("i dont understand that")

        enter3 = input(">")
        if enter3 == "Quit" or "quit":
            print()
            break
        counter += 1
   #
