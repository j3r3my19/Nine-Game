# Nine-Game

Welcome to this awesome local multiplayer cards game. As I was not able to find the rules online (this game may have been invented by a friend, that's the legend), you can find the rules at the end of the readme.

## Install

1. Install required packages

```bash
pip install -r requirements.txt
```

2. Start the game

```bash
python run main.py
```

3. Initialize the game

Set the number of players (6 max)
Set the names of players and confirm
A local window starts and the game begins !

## Rules

Gameplay:
Rounds: The game is played over multiple rounds. In each round:
Cards are dealt to players (5 cards each).
One card is drawn to start the pile.

Player Actions:
Players take turns drawing and playing cards.
Players can draw from either the deck or the pile.
The goal during a player's turn is to play a set of cards according to the rules (one card, suits, pair, triple...).
Players may pass their turn only one time per round.

Ending a Round:
A round ends when one player finishes their play (9 or less in its hand).
Scores are calculated and displayed at the end of each round. 
If a player’s score reaches or exceeds the elimination threshold, they are marked as eliminated.
The order of play is rotated for the next round.

Elimination:
If a player's score reaches or exceeds 150 points, they are eliminated from the game.
Players continue to be eliminated round by round until only one player remains.

End of Game:
The game concludes when only one player is not eliminated. A final score table is displayed at the end.

Card Values:
Ace: 1 point,
King, Queen, Jack, 10: 10 points each,
9: 9 points,
8: 8 points,
7: 7 points,
6: 6 points,
5: 5 points,
4: 4 points,
3: 3 points,
2: 2 points,
Joker: -1 point,
