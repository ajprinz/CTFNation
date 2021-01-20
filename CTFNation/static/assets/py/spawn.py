# Spawn

import os
import random, string
import json

dir = ["/home/mysexysparkles/Desktop/red"]


def spawnFlags(teams):
    for i in range(len(teams)):
        with open(os.path.join(dir[0], teams[i] + "-flag.txt"), "w") as file:
            teamFlag = "flag-" + teams[i] + "-" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            file.write(teamFlag)


def spawnPlayers(players):
    for i in range(len(players)):
        with open(os.path.join(dir[0], players[i] + ".txt"), "w") as file:
            userFlag = "flag-" + players[i] + "-" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            file.write(userFlag)


if __name__ == "__main__":

    # Initial game setup
    # Exampe array passed to server
    array = '{"teams": ["red", "blue"], "red": ["mysexysparkles", "savouryshoe"],"blue": ["wheatgerm", "sirfish"]}'
    game = json.loads(array)

    # Spawn the team flags
    spawnFlags(game["teams"])

    # Spawn players per team
    spawnPlayers(game['red'])
    spawnPlayers(game['blue'])
