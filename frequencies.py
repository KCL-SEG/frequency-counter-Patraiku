"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if(str(item) not in frequencies.keys()):
            frequencies[str(item)] = 1
        else:
            frequencies[str(item)] = frequencies[str(item)] + 1
    return frequencies
