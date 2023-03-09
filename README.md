Python development project template
===================================

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

About the game:(hampus)
---------------

fitures of our game:(abdullah)
--------------------
When the game starts the user/s can choose to play the game, see scores, change a name which is stored in the txt
file or exit the game.
After choosing to play the game the user can choose to play against computer and if so the user can choose the level
of intelligence of the computer which are: Level1 random cards, level2 random cards but the first card is the highest
card in the deck eccept 1 and level3 random cards but the first two cards are the highest cards in the deck eccept 1,
or against another player.
Each human player can flipp, use hack to steal 1 or 2 cards from the opponent, continue the game automatically untill
a winner is found or exit the game.

How to install the game:(hampus)
------------------------


How to run the game:(hampus)
--------------------


How to create and run the virtual environment:(hampus)
-----------------------------------


How to install make and chocolati:(hampus)
----------------------------------


How to do testings:(abdullah)
----------------
After installing gitbash, chocolati, make on the computer  and creating the vertual environment in the game folder which
you downloaded from git hub, you need to install the requirenments.txt on the venv, you do that by oppening git bash in
directory of the game folder then activate venv by using (". .venv/Scripts/activate") then ("make install").
After installing what is in the requirenment.txt you can use:
1- ("make flake8") to test the game files using flake8
2- ("make pylint") to test the game files using pylint
3- ("make coverage") to do coverage
4- ("coverage report -m") to see the coverage report
5- ("make test") to run flake8, pylint tests and coverage at the same time
When you finish your tests and coverage you can close the vetual environment using ("deactivate").


How to generate uml:(abdullah)
-------------------


How to generate html:(abdullah)
--------------------

