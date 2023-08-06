from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.8.0'
DESCRIPTION = 'Realtion match percentage calculator'
LONG_DESCRIPTION = '''

# lovematch

The `lovematch` library is a Python package that allows you to calculate friendship and love match percentages between given names.

## Installation

You can install `lovematch` using pip, the Python package manager:

```bash
pip install lovematch
```


## Usage
### You can use lovematch in your Python code as follows:


```python
from lovematch.friendship import calculate_frindship_match_percentage
from lovematch.love import calculate_love_match_percentage

# Calculate friendship match percentage
your_name = "Alice"
friend_name = "Bob"
friendship_percentage = calculate_frindship_match_percentage(your_name, friend_name)
print(f"Friendship match percentage between {your_name} and {friend_name}: {friendship_percentage}")

# Calculate love match percentage
your_name = "Alice"
partner_name = "Bob"
love_percentage = calculate_love_match_percentage(your_name, partner_name)
print(f"Love match percentage between {your_name} and {partner_name}: {love_percentage}")
```

'''



# Setting up
setup(
    name="lovematch",
    version=VERSION,
    author="Devendra Parihar",
    author_email="devendraparihar340@gmail.com",
    url="https://github.com/Devparihar5/lovematch",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'love', 'match', 'percentage', 'calculator', 'lovematch'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)