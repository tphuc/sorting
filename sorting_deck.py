#!/usr/bin/env python3
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('--gui', action = 'store_true')
argparser.add_argument('N', type = int, nargs = "*")
argparser.add_argument('--algo', default = 'bubble')
args = argparser.parse_args()
args = vars(args)
CHOICES = ['bubble','quick','insert','merge']

def processArguments(args):
    if not len(args['N']):
        print("sage: sorting_deck.py [-h] [--algo ALGO] [--gui] N [N ...]")
        print("sorting_deck.py: error: the following arguments are required: N")
        return 0
    algo = args['algo'] 
    should_display = False
    if args['gui'] and len(args['N']) <= 15:
        should_display = True 
    return (algo, should_display, args['N'])
def bubble():
    return 'bubble'
def quick():
    return 'quick'
def merge():
    return 'merge'
def insert():
    return 'insert'


def deployAlgorithm(option):
    switcher = {'bubble':bubble,'quick':quick,'insert':insert,'merge':merge}
    return switcher[option]()

if __name__ == '__main__':
    algoithm = processArguments(args)[0]
    