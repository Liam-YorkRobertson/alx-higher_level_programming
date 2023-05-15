#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)
    if sentence_len > 0:
        first_character = sentence[0]
    else:
        "None"
    sentence_tuple = sentence_len, first_character
    return (sentence_tuple)
