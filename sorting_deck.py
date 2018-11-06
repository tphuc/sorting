#!/usr/bin/env python3
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('--gui', action = 'store_true')
argparser.add_argument('N', type = int, nargs = "*")
argparser.add_argument('--algo', default = 'bubble')
args = argparser.parse_args()
args = vars(args)
CHOICES = ['bubble','quick','insert','merge']
def print_list(data, pivot = 0):
    CRED = '\033[91m'
    CEND = '\033[0m'
    for i in data:
        if i == pivot:
            print(CRED+str(i)+CEND, end=" ")
        else:
            print(i, end=" ")
    print("")
def processArguments(args):
    if not len(args['N']):
        print("sage: sorting_deck.py [-h] [--algo ALGO] [--gui] N [N ...]")
        print("sorting_deck.py: error: the following arguments are required: N")
        return 0
    algo = args['algo'] 
    gui = False
    if args['gui'] and len(args['N']) <= 15:
        gui = True 
    return (algo, gui, args['N'])

def bubble(data):
    """ perform bubble sort """
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            print_list(data)

def quick(data, left=0, right=None):
    print_list(data)
    if right == None:
        right = len(data) - 1
    if left >= right:
        return
    """------------------ """
    middle = int((right+left)/2)

    pivot = data[middle]  # pick the Pivot
    print("P:",pivot," L M R: ", left, middle, right)
    i = left
    j = right

    while True:
        while data[i] < pivot and i <= j:
            i+=1
        while data[j] > pivot and j >= i:
            j-=1
        if i == j:
            print_list(data, pivot)
            print("break----------")
            break
        else:
            print('swap:', data[i], data[j])
            data[i], data[j] = data[j], data[i]
            print_list(data, pivot)
    print(i,j)
    print_list(data, pivot)
    print("")
    quick(data, left, i-1)
    quick(data, i+1, right)


def merge(data):
    if len(data) >1: 
        mid = len(data)//2 #Finding the mid of the dataay 
        L = data[:mid] # Dividing the dataay elements  
        R = data[mid:] # into 2 halves 
  
        merge(L) # Sorting the first half 
        merge(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp dataays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                data[k] = L[i] 
                i+=1
            else: 
                data[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            data[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            data[k] = R[j] 
            j+=1
            k+=1

def insert(data):
    data = data
    for i in range(1, len(data)): 
        current = data[i] 
        j = i-1 # set the start point to reverse check
        while j >= 0:
            if current < data[j]:
                data[j+1] = data[j]
                j -= 1
            else:
                break
        data[j+1] = current
        print_list(data)

def DeployAlgorithm(ARGS):
    switcher = {'bubble':bubble,'quick':quick,'insert':insert,'merge':merge}
    return switcher[ARGS[0]](ARGS[2])

if __name__ == '__main__':
    ARGS = processArguments(args)
    DeployAlgorithm(ARGS)