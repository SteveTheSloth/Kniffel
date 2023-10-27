# Multiple Versions of the Multiplayer Dice Game 'Kniffel'

This project has stuck with me for the entire duration of my programming studies up to this day. This game is very similar to the more popular Yahtzee. I coded version 1 in 2021 and version 6 in 2023 (not included in this repository but playable on my website: https://lvcodes.de/projects/kniffel/game and included in the github repository for said website: https://github.com/SteveTheSloth/Website).

## Game Rules

Try to score as many points as possible by filling in your scoresheet. You can only complete each field of your scoresheet once. At the end of the game you will have played 13 rounds and filled in your entire scoresheet (the fields 'Bonus', 'Total Top', and 'Total' are calculated automatically and can't be filled in by the player). If your roll doesn't fit any of your open fields (or you don't want to take it), you choose one field to cross off. You get to roll your dice 3 times per round. To keep dice that you don't want to reroll, simply click on the die.

## Scoring

Top section: only multiples of the given number are added up. Get at least 63 points (equal to 3 of each dice value) to receive a bonus of 35 points.

Three of a Kind and Four of a Kind: roll includes at least 3/4 dice of the same value. Entire roll is added up.

Full House: roll includes 3 dice of the same value and 2 dice of the same value. 5 identical values can also count as a Full House.

Small Street and Big Street: roll contains 4/5 consecutive values.

Kniffel: 5 dice of the same value

Chance: entire roll is added up without restrictions.

# Version 1 - Functional Programming

This version is completely text-based and requires abstract keyboard inputs to work. It is functionally programmed and consists of one individual file. It does not incorporate all of the game's mechanics and is certainly not bug-free.

## Installation

To play the game, simply clone the repository, open a terminal, cd into the corresponding directory and run **python Kniffel_v1.py**. No further installations required.

```bash
cd .../Kniffel/
python Kniffel_v1.py

```

## Usage

The game's output should be self-explanatory, although not particularly well formatted. Some of the text-output is in German.

# Version 2 - Object Oriented Programming

This version shows my first steps in Object Oriented Programming. I split the game into three modules containing parts of the game logic represented by class definitions and methods. The game is still represented by text input and output in the terminal, but with improved formatting. It is still an incomplete adaptation of the game and not bug-free.

## Installation

To play the game, clone the repository, open a terminal, cd into the corresponding directory and run **python objects.py**. No further installations required.

```bash
cd .../Kniffel_v2/
python objects.py

```

## Usage

Very similar to v1 with improved formatting.

# Version 3 - Graphical User Interface with Pygame

This version shows my first implementation of a Graphical User Interface. It uses pygame to create a fully playable and reasonably well working version of the game that does not rely on terminal in- and outputs anymore. All of the game's mechanics are implemented and I have not found any bugs while testing.

## Installation

Cd into the corresponding directory, create a virtual environment using pipenv, install dependencies, and run **python main.py**

```bash
cd .../Kniffel_v3/
pipenv shell
pipenv install -r requirements.txt
python main.py
```

## Usage

Input player names on the first screen and click 'Continue'. Click 'Roll' to roll dice, click on dice to keep them for your next roll. To take a scoring option, click on the marked option.

# Version 4 - Model View Controller Paradigm & Graphical User Interface with PyQt

This version shows my first steps trying to implement the MVC paradigm. I tried to reorganise the game code to be more easily adaptable to different ways of displaying. I used PyQt to create a new GUI. This GUI is a step down from the previous version with regards to intuitivity as I did not spend enough time on learning how to properly use PyQt. This version was primarily intended as an exercise in implementing the paradigm and stepping away from the rarely used Pygame library. I added several new functionalities like the possibility to save and load games and create new lists to score multiple games with the same players. While there are some uncaught bugs (e.g. trying to load a game while no saved games exist causes the game to crash), these functionalities work well for the most part and are implemented using Openpyxl.

## Installation

Cd into the corresponding directory, create a virtual environment using pipenv, install dependencies, and run **python loop.py**

```bash
cd .../Kniffel_v4/
pipenv shell
pipenv install -r requirements.txt
python loop.py
```

## Usage

Input player names on the first screen and click 'Continue'. Click 'Roll' to roll dice, click 'Keep' to open popup with selectable dice values, click 'Cross' to choose from possible crossing options, click 'Take' to choose from possible scoring options. To see current scoresheet, hover over player name.

# Version 5 - First Steps in Reinforcement Learning with Stable Baselines

This is less a seperate version of the game and more an experiment based on the previous ones. While this was a very challenging and exciting learning experience it is the only part of this repository, that I consider a failure. I set out to train a machine learning model to become as good or even better than a human player at the game Kniffel and failed. I managed to train models, and to gain an insight into the world of reinforcement learning but although I tried many different ways of training the models and experimented a lot with the Stable Baselines library, I had too little knowledge of the basics of machine learning to produce any satisfying results. I also lacked the necessary resources to change that.

After realising that my initial approach of training one model with a simple point-threshold reward strategy did not yield any satisfying results, I tried to implementing other, more nuanced reward strategies (e.g. based on the current game state and roll results). This also did not prove to be successful. I then tried to train models based on individual score-fields (e.g. as many sixes as possible or roll a street) and implement another model that was supposed to only make the top-level decision of which model to chose given a certain roll. While I was able to achieve satisfying result for models trained to roll for a certain score-field, combining those two levels still did not result in any satisfying overall scores. I decided to drop this experiment, as I wanted to focus my studies on other areas.

## License

[MIT](https://choosealicense.com/licenses/mit/)
