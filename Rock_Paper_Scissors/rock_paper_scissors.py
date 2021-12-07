import random
var = random.choice(["rock", "scissors", "paper"])
a = input("• ")
if a == var:
    print(f"There is draw ({a})")
if a == "scissors" and var == "rock":
    print(f"Sorry, but the computer chose {var}")
if a == "scissors" and var == "paper":
    print(f"Well done. The computer chose {var} and failed")
if a == "rock" and var == "scissors":
    print(f"Well done. The computer chose {var} and failed")
if a == "rock" and var == "paper":
    print(f"Sorry, but the computer chose {var}")
if a == "paper" and var == "scissors":
    print(f"Sorry, but the computer chose {var}")
if a == "paper" and var == "rock":
    print(f"Well done. The computer chose {var} and failed")
