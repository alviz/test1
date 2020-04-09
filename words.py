#! /usr/bin/env python3.8

""" Hello world
    it's main help

"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """ Function to grab url site.

        Arg:
           url - web page

        Return:
           bla-blabla
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


if __name__ == '__main__':
    url = sys.argv[1]
    words = fetch_words(url)
    print_words(words)
