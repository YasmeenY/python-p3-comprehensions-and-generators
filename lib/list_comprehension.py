#!/usr/bin/env python3

def return_evens(num_list):
    lists = [n for n in num_list if n%2 == 0]
    return (lists)

def make_exclamation(sentence_list):
    exclaim_all = [f"{sentence}!" for sentence in sentence_list]
    return (exclaim_all)