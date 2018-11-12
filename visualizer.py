import pyglet
import time
WIDTH = 1000
HEIGHT = 1000

delta_sec = 0.02
t_quick = 4
t_bubble = 2
t_insert = 2


class Plot:
    """ List of Nums on screen """
    def __init__(self, list_Num):
        self.nums = list_Num
        self.stack_swap = []
        self.stack_active = []
        self.stack_sorted = []
        self.stack_pivot = []

    def check_finish(self):
        if not len(self.stack_swap):
            for num in self.nums:
                num.sorted = True
                num.set_marked()
            return True
        else:
            return False

    def visualize(self,arg):
        if arg == 'quick':
            self.visual_quick()
        elif arg == 'insert':
            self.visual_insertion()
        else:
            self.visual_bubble()

    def draw(self):
        for num in self.nums:
            num.draw()

    def move(self):
        for num in self.nums:
            num.move(num.velc)

             
    def swap(self,dt):
        if len(self.stack_swap) > 1:
            Num.swap(self.stack_swap[0], self.stack_swap[1])
            """ pop 2 first elements from swap stack """
            self.stack_swap = self.stack_swap[2:]

    #############################
    def visual_insertion(self):
        for i in range(1, len(self.nums)):
            current_num = self.nums[i] 
            current = self.nums[i].val 
            j = i-1 # set the start point to reverse check
            while j >= 0:
                if current < self.nums[j].val:
                    self.nums[j+1], self.nums[j] = self.nums[j], self.nums[j+1]
                    #print(j,':',self.nums[j].val,j+1,':',self.nums[j+1].val)
                    self.stack_swap.append(self.nums[j])
                    self.stack_swap.append(self.nums[j+1])
                    self.stack_sorted.append(current_num)
                    j -= 1
                else:
                    break
        pyglet.clock.schedule_interval(self.tick_insert, t_insert)
    
    def tick_insert(self,dt):
        if len(self.stack_sorted) > 0:
            self.stack_sorted[0].sorted = True
            self.stack_sorted[0].set_marked()

        pyglet.clock.schedule_once(self.swap, 0.5)
        self.stack_sorted = self.stack_sorted[1:]
        """ finished """
        if self.check_finish():
            pyglet.clock.unschedule(self.tick_insert)

    ###################################
    def visual_bubble(self):
        """ perform bubble sort with visualization """
        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                if j != len(self.nums)-i-2:
                    self.stack_sorted.append(0)

                self.stack_active.append(self.nums[j])
                self.stack_active.append(self.nums[j+1])
                if self.nums[j].val > self.nums[j+1].val:
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
                    
                    self.stack_swap.append(self.nums[j])
                    self.stack_swap.append(self.nums[j+1])
            self.stack_sorted.append(1)
        """ ticking bubble sort """
        pyglet.clock.schedule_interval(self.tick_bubble, t_bubble)

    def tick_bubble(self, dt):
        if len(self.stack_active) > 1:
            """ set active 2 current elements to compare """
            self.stack_active[0].set_active()
            self.stack_active[1].set_active()
            """ set deactive other elements """
            for i in range(2,len(self.stack_active)):
                if self.stack_active[i] != self.stack_active[0] and self.stack_active[i] != self.stack_active[1]:
                    self.stack_active[i].set_active(False)
            """ check if can swap """
            if set(self.stack_active[:2]) == set(self.stack_swap[:2]):
                pyglet.clock.schedule_once(self.swap, 0.5)
            
            """ marked the sorted every loop """
            if self.stack_sorted[0]:
                self.stack_active[0].sorted = True

                if len(self.stack_swap) == 0:
                    for num in self.stack_active:
                        num.sorted = True
                        num.set_marked()
            """ pop the element from its stack """ 
            self.stack_sorted = self.stack_sorted[1:]
            self.stack_active = self.stack_active[2:]
        """ finished """
        if self.check_finish():
            pyglet.clock.unschedule(self.tick_bubble)
    #############################################
    def visual_quick(self, left=0, right=None):
        if right == None:
            right = len(self.nums) - 1
        if left >= right:
            if right == len(self.nums)-1:
                pyglet.clock.schedule_interval(self.tick_quick, t_quick)
            return
        """------------------ """
        middle = int((right+left)/2)
        pivot_num = self.nums[middle]
        pivot = self.nums[middle].val  # pick the Pivot
        print("P:",pivot)
        i = left
        j = right

        while True:
            while self.nums[i].val < pivot and i <= j:
                i+=1
            while self.nums[j].val > pivot and j >= i:
                j-=1
            if i == j:
                break
            else:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                self.stack_swap.append(self.nums[i])
                self.stack_swap.append(self.nums[j])
                self.stack_pivot.append(pivot_num)
                self.stack_pivot.append(pivot_num)
        self.visual_quick(left, i-1)
        self.visual_quick(i+1, right)

    def tick_quick(self, dt):
        if len(self.stack_pivot) > 0:
            """ set active 2 current elements to compare """
            self.stack_pivot[0].set_marked()
            self.stack_pivot[1].set_marked()
            """ set deactive other elements """
            for i in range(2,len(self.stack_pivot)):
                if self.stack_pivot[i] != self.stack_pivot[0] and self.stack_pivot[i] != self.stack_pivot[1]:
                    self.stack_pivot[i].set_active(False)
        pyglet.clock.schedule_once(self.swap, 0.5)
        self.stack_pivot = self.stack_pivot[2:]
        """ finished """
        if self.check_finish():
            pyglet.clock.unschedule(self.tick_quick)
    ############################################################
class Color:
    red = (255,0,0,255)
    green = (0,255,0,255)
    blue = (0,0,255,255)
    white = (255,255,255,255)
    orange = (255,165,0,255)
    pink = (255,105,180,255)
    dim = (105,105,105,125)
    active = (0,255,0,255)
    sort = (255,255,0,255)

class Num:
    gap = 50
    speed = 5
    def swap(obj1, obj2):
        obj1.move_to(obj2.loc)
        obj2.move_to(obj1.loc)
        #obj1.set_active()
        #obj2.set_active()
        #obj1.val , obj2.val = obj2.val, obj1.val


    def __init__(self, val, loc, size, color=(255,255,255,255)):
        self.val = val
        self.loc = loc
        self.color = color
        self.size = size
        self.pylabel = pyglet.text.Label(str(self.val),
                          x=self.loc[0], y=self.loc[1],
                          anchor_x='center', anchor_y='center',
                          color=color)
        self.velc = (0, 0)
        self.target_loc = None
        self.sorted = False

    """ ########### Moving ################"""
    ######################################################
    ######################################################
    def move(self,velc):
        """ consistent move the text along x, y unit """
        self.pylabel.x += velc[0]
        self.pylabel.y += velc[1]

    def stop(self):
        self.velc = (0,0)
        self.update_location()
        if self.sorted:
            self.set_marked()



    def move_to(self,location):
        self.update_targetlocation(location)
        #deltaX = location[0] - self.pylabel.x
        #deltaY = location[1] - self.pylabel.y
        """
        if avoid:
            if deltaX > 0:
                self.velc = (0,unit_move(50,1))
                pyglet.clock.schedule_once(self.move_horizontal,1)
                pyglet.clock.schedule_once(self.move_down,1.5)
                pyglet.clock.schedule_once(self.stop,2.5)
            else:
                self.velc = (0,unit_move(-50,1))
                pyglet.clock.schedule_once(self.move_horizontal,1)
                pyglet.clock.schedule_once(self.move_up,1.5)
                pyglet.clock.schedule_once(self.stop,2.5)
        """
        if location[0] > self.pylabel.x:
            self.move_right()
        else:
            self.move_left()
        pyglet.clock.schedule_interval(self.check_has_arrived, 0.01)

    def update_targetlocation(self, location):
        self.target_loc = location

    def update_location(self):
        self.loc = (self.pylabel.x, self.pylabel.y)

    def move_right(self):
        self.velc = (Num.speed,0)
    
    def move_down(self):
        self.velc = (0,Num.speed*-1)

    def move_left(self):
        self.velc = (Num.speed*-1,0)

    def move_up(self):
        self.velc = (0,Num.speed)

    def check_has_arrived(self,dt):
        if nearly_equal(self.pylabel.x, self.target_loc[0]) and nearly_equal(self.pylabel.y, self.target_loc[1]):
            self.stop()
            pyglet.clock.unschedule(self.check_has_arrived)
    ###########################################################################
    ###########################################################################

    def draw(self):
        self.pylabel.draw()

    def delete(self):
        self.pylabel.delete()

    def resize(self,size):
        self.pylabel.size = size

    def change_color(self, color):
        self.pylabel.color = color

    def set_active(self, active=True):
        if active:
            self.change_color(Color.green)
        else:
            self.change_color(Color.white)

    def set_marked(self):
        self.change_color(Color.orange)

    def update_value(self):
        self.pylabel.text = str(self.val)

def get_start_location(n):
    global WIDTH, HEIGHT
    return ((WIDTH - n*Num.gap)/2, HEIGHT/2)



def nearly_equal(float1, float2, error_tol=1):
    return float1 >= float2 - abs(error_tol) and float1 <= float2 + abs(error_tol)


def unit_move(d,time):

    return d/time*delta_sec



