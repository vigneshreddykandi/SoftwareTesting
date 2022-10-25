#vignesh reddy kandi
import random

Com = random.choice(["Paper", "Rock",  "Scissors"])


def Defeat1(You, Com):
    if You == "Paper" and Com == "Scissors":
        return "Better luck next time :3"

def Defeat2(You, Com):
    if You == "Rock" and Com == "Paper":
        return "Better luck next time :3"

def Defeat3(You, Com):
    if You == "Scissors" and Com == "Rock":
        return "Better luck next time :3"


def Victory1(You, Com):
    if You == "Scissors" and Com == "Paper":
        return "Will get you next time"

def Victory2(You, Com):
    if You == "Paper" and Com == "Rock":
        return "Will get you next time"

def Victory3(You, Com):
    if You == "Rock" and Com == "Scissors":
        return "Will get you next time"


def Tie(You, Com):
    if You == Com:
        return "Try again"


def false(You, Com):
    try:
        str(You, Com)
        return True
    except:
        return False

