class Interact:
    @staticmethod
    def get_binary_input(text):
        x = input(text)
        if x == "y":
            return True
        elif x == "n":
            return False
        else:
            return x

    @staticmethod
    def get_string_input(text):
        return input(text)

    @staticmethod
    def get_scoresheet_input():
        text = "Do you want to use the standardized kniffel scoresheet? (y/n) "
        return Interact.get_binary_input(text)

    @staticmethod
    def get_more_players_input():
        text = "Do you want to add more players? (y/n) "
        return Interact.get_binary_input(text)

    @staticmethod
    def get_playername_input(index):
        return input(f"What is the name of player number {index}? ")

    @staticmethod
    def get_decision():
        x = input("What do you want to do? (roll, keep, take, cross) ")
        if x == "roll":
            return 1
        if x == "keep":
            return 2
        if x == "take":
            return 3
        if x == "cross":
            return 4
        else:
            return 0

    @staticmethod
    def maxrolls_reached():
        print("Maximum number of rolls reached.")

    @staticmethod
    def get_keep_dice():
        x = input(
            "Which dice do you want to keep? (Nr. of dice seperated by comma, i.e.: 1, 3, 5) "
        )
        x = x.split(",")
        try:
            x = [int(i) for i in x]
            return x
        except:
            return []

    @staticmethod
    def get_take_option(options):
        Display.show_options(options)
        x = int(
            input(
                "Which option do you want to take? (enter the first number on the line of your chosen option)"
            )
        )
        value = options.get(x, None)
        if value == None:
            print("Please enter a valid option.")
            Interact.get_take_option(options)
        else:
            return (x, value[0], value[1])

    @staticmethod
    def get_cross_option(options):
        Display.show_options(options)
        x = int(input("Which options do you want to cross off? "))
        value = options.get(x, None)
        if value == None:
            print("Please enter a valid option.")
            Interact.get_cross_option(options)
        else:
            return (x, "X", value[1])


class Display:
    @staticmethod
    def show_end_scores(playerlist):
        print(
            f"{playerlist[0].name} has won with {playerlist[0].scored[15][0]} points!"
        )
        for i in playerlist[1:]:
            print(f"{i} has {i.scored[15][0]} points.")

    @staticmethod
    def show_options(options):
        for key, value in options.items():
            print(key, ":  ", value[0], "\t", value[1])

    @staticmethod
    def show_roll(player):
        print([x.value for x in player.mydice])
