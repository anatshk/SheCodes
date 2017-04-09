"""
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
"""

from Exercises.lecture_11.rock_paper_scissors.game import Game
from Exercises.lecture_11.rock_paper_scissors.agent import InstructorAgent, MyAgent, HumanAgent


# We can specify which agents we want to play the game here
# Optional: pass this in using the command line
# game = Game(InstructorAgent(), InstructorAgent())
# game = Game(HumanAgent(), InstructorAgent())
game = Game(MyAgent(), InstructorAgent())

# How many rounds do we want to play
# Optional: pass this in using the command line
number_rounds = 100
game.play(number_rounds)

# Print summary
game.summary()
