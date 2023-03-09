Python development project template
===================================

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Description:
------------

This card game 'War' is a group project created by Abdullah Mallah, Eszter Kalmár and Hampus Gunnarsson.

The basic idea is that the game is played by two players using a standard deck of 52 cards.
The objective of the game is to win all of the cards.

Players start by evenly dividing the deck between themselves and then each player turns over their top card. 
The player with the highest card wins both cards and adds them to the bottom of their deck.

If there is a tie, a "war" occurs where each player puts three cards face down and then turns over another card.
The player with the highest card wins all the cards in the tie. The game continues until one player has won all the cards.

Features of our game:(abdullah)
-------------------------------
When the game starts the user/s can choose to play the game, see scores, change a name which is stored in the txt
file or exit the game.
After choosing to play the game the user can choose to play against computer and if so the user can choose the level
of intelligence of the computer which are: Level1 random cards, level2 random cards but the first card is the highest
card in the deck eccept 1 and level3 random cards but the first two cards are the highest cards in the deck eccept 1,
or against another player.
Each human player can flipp, use hack to steal 1 or 2 cards from the opponent, continue the game automatically untill
a winner is found or exit the game.

Installing the game:
------------------------
Start by installing the latest version of python3 if you dont have it installed already:
https://www.python.org/downloads/

Start by downloading the repo, either as a zip-file or using git clone.
https://github.com/abdullah-mallah/war-card-game-examination2-sustainableProgramming.git

How to run the game:(hampus)
----------------------------
Open your terminal and change directory to where you saved the 

How to create and run the virtual environment:
----------------------------------------------
Create and use the virtual venv using:
--------------------------------
make venv

- If you use a Python installation on Window, then activate like this:

. .venv/Scripts/activate

- If you use a Python installation on Mac/Linux, then activate like this:

. .venv/bin/activate

Do not forget to deactivate when you are done using:
deactivate


How to install make and chocolatey:
-----------------------------------
The Make command and the Makefiles are in general used to compile, build and run programs and tasks.

Ensure that you have it installed in your terminal, it should already be installed on Linux/Mac.

You can check your current version like this.
$ make --version
"GNU Make 4.3"

If you do not have it installed then using the Windows package manager chocolatey is one way to do this. 
You will then install the make command within Windows and it can then be used from Git Bash.

Follow the following steps to install Git Bash, Chocolatey and Make:

1. Start by installing Git Bash on Windows using this link - https://gitforwindows.org/
2. Install the Windows packet manager Chocolatey - https://chocolatey.org/install
3. Install GNU make using 'choco install make' using PowerShell (you might need to run the terminal as admin).
4. Open a new window for Git Bash and check that it works be checking what version you have using make --version.


How to do testings:
-------------------
After installing git bash, chocolatey, make on the computer  and creating the virtual environment in the game folder which
you downloaded from git hub, you need to install the requirenments.txt on the venv, you do that by opening git bash in
directory of the game folder then activate venv by using (". .venv/Scripts/activate") then ("make install").
After installing what is in the requirenment.txt you can use:
1- ("make flake8") to test the game files using flake8
2- ("make pylint") to test the game files using pylint
3- ("make coverage") to do coverage
4- ("coverage report -m") to see the coverage report
5- ("make test") to run flake8, pylint tests and coverage at the same time
When you finish your tests and coverage you can close the virtual environment using ("deactivate").

How to generate documentation and HTML:
---------------------------------------
After oppening git bash in the game file and activating venv you need to use ("make doc") to generation documentation of the
game

How to generate UML:
-------------------
After opening the virtual environment in the path of the game and activate it and generating documentation you need to
use ("pip install graphviz") then ("pyreverse classes/*.py") then:
1- ("dot -Tpng classes.dot -o doc/pyreverse/classes.png") to generate uml of the classes.
2- ("dot -Tpng packages.dot -o doc/pyreverse/packages.png") to generate uml of packages.
If for some reason step 1 or 2 did not work then just create a folder with the name "doc" in the game folder then do step 1 and 2.

Other useful commands:
----------------------
1- ("make --version") to check if make is installed on your computer and which version is installed.
1- ("choco --version") to check if chocolatey is installed on your computer and which version is installed.
