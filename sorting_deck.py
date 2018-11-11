#!/usr/bin/env python3
import argparse
from visualizer import *
CHOICES = ['bubble','quick','insert','merge']
def print_list(data, pivot = 0):
    CRED = '\033[91m'
    CEND = '\033[0m'
    for i in data:
        if i == pivot:
            print(i, end=" ")
        else:
            print(i, end=" ")
    print("")

def bubble(data):
    temp_data = data.copy()
    if not temp_data.sort() == data:
        """ perform bubble sort """
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    print_list(data)

def quick(data, left=0, right=None):
    if right == None:
        right = len(data) - 1
    if left >= right:
        return
    """------------------ """
    middle = int((right+left)/2)

    pivot = data[middle]  # pick the Pivot
    print("P:",pivot)
    i = left
    j = right

    while True:
        while data[i] < pivot and i <= j:
            i+=1
        while data[j] > pivot and j >= i:
            j-=1
        if i == j:
            break
        else:
            data[i], data[j] = data[j], data[i]

    print_list(data, pivot)
    quick(data, left, i-1)
    quick(data, i+1, right)


def merge(data):

    if len(data) >1: 
        mid = len(data)//2 #Finding the mid of the data
        L = data[:mid] # Dividing the data elements  
        R = data[mid:] # into 2 halves 
  
        merge(L) # Sorting the first half 
        merge(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp data L[] and R[] 
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
        print_list(data)


def insert(data):
    for i in range(1, len(data)):
        temp_data = data.copy() 
        current = data[i] 
        j = i-1 # set the start point to reverse check
        while j >= 0:
            if current < data[j]:
                data[j+1] = data[j]
                j -= 1
            else:
                break
        data[j+1] = current
        if temp_data != data:
            print_list(data)




def DeployAlgorithm(algo, data):
    if algo == 'quick':
        quick(data)
    elif algo == 'bubble':
        bubble(data)
    elif algo == 'insert':
        insert(data)
    elif algo == 'merge':
        merge(data)

def process_argument_parser():
    """ return the dict for args """
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--gui', action = 'store_true')
    argparser.add_argument('N', type = int, nargs = "*")
    argparser.add_argument('--algo', default = 'bubble')
    args = argparser.parse_args()
    args = vars(args)
    if not len(args['N']):
        print("sage: sorting_deck.py [-h] [--algo ALGO] [--gui] N [N ...]")
        print("sorting_deck.py: error: the following arguments are required: N")
        return 0
    algo = args['algo'] 
    gui = False
    if args['gui']:
        if len(args['N']) <= 15:
            gui = True
        else:
            print("Input too large")
            return 0
    return (algo, gui, args['N'])


    

if __name__ == '__main__':
    args = process_argument_parser()
    if not args == 0:
        ALGO = args[0]
        GUI = args[1]
        data = args[2]
        vis_data = data.copy()
        DeployAlgorithm(ALGO,data)
        start_width = get_start_location(len(data))[0] 

        Algo_label = pyglet.text.Label(str(ALGO)+' sort',
                          x=450, y=800, font_size=36, bold = True,
                          anchor_x='center', anchor_y='center',
                          )
    
        if GUI:
            window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
            Nums = []
            for i in range(len(vis_data)):
                Nums.append(Num(vis_data[i],(start_width+Num.gap*i,HEIGHT/2+100),30))
            Batch = Plot(Nums)
            @window.event
            def on_draw():
                window.clear()
                Batch.draw()
                Algo_label.draw()

            def update(dt):
                Batch.move()
                pass

            def start(dt):
                Batch.visualize(ALGO)
                pass

            

            pyglet.clock.schedule_interval(update, 0.02)
            
            pyglet.clock.schedule_once(start,0)
            pyglet.app.run()
    