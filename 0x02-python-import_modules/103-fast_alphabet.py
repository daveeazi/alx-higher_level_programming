#!/usr/bin/python3

def lowercaseAlphabets():

    for c in range(97, 123):
        print(chr(c), end = " ");

    print("");

def uppercaseAlphabets():

    for c in range(65, 91):
        print(chr(c), end = " ");

    print("");

uppercaseAlphabets();
lowercaseAlphabets();
