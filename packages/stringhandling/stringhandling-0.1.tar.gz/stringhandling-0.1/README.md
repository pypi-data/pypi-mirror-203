README.txt

Introduction:- Python package for string handling

Usage:- use pip to install stringhandling. pip install stringhandling after installation you are ready to use the functions in this package.

e.g.,

to extract the words list from a sentence / paragraph, use the function 'get_words_list()'

from stringhandling import strhandle

paragraph = """package to manage sentence or paragraph package to manage sentence or paragraph package to manage sentence or paragraph""" words = []

words = strhandle.get_words_list(paragraph)

Output:- ['package', 'to', 'manage', 'sentence', 'or', 'paragraph', 'package', 'to', 'manage', 'sentence', 'or', 'paragraph', 'package', 'to', 'manage', 'sentence', 'or', 'paragraph']