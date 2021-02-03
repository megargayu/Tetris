# Tetris
This is a simple remake of the infamous Tetris game (that I am sure you have heard of). Use the left and right arrow keys to move the piece left and right, the up arrow to rotate the piece, and the space bar to hard drop or hold the down arrow to soft drop.

## Installing
1. Install [Python 3.9.1](https://www.python.org/downloads/release/python-391/) on your system
2. Run `pip install -r requirements.txt` in the directory you downloaded this in
3. Run `python player_gui.py` in the directory you downloaded this in to run
4. Enjoy!

### Scoring system
The number of lines you remove is corresponding to the number of points you get. Here are all the values:

| Lines Cleared | Score                                 |
| ------------- | ------------------------------------- |
| 0             | 0                                     |
| 1             | 100                                   |
| 2             | 300                                   |
| 3+            | 500 x (number of lines cleared - 2)   |
