# pylovemeter

`pylovemeter` is a Python library that provides functions for calculating love and friendship scores based on input names.

## Installation

You can install `pylovemeter` using pip:



## Usage

```python
from pylovemeter import love_score, friendship_score

# Calculate love score
boy_name = "Romeo"
girl_name = "Juliet"
love_percentage = love_score(boy_name, girl_name)
print(f"Love score between {boy_name} and {girl_name}: {love_percentage}%")

# Calculate friendship score
friend1 = "Alice"
friend2 = "Bob"
friendship_percentage = friendship_score(friend1, friend2)
print(f"Friendship score between {friend1} and {friend2}: {friendship_percentage}%")
