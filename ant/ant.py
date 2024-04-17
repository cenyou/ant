import random
import abc
import numpy as np

class Ant(abc.ABC):
    def __init__(
        self,
        speed=10,
        seed=0,
    ):
        self.__speed = speed
        random.seed(seed)
        self.__state = {'time': 0, 'location': np.array([0, 0])}

    def reset(self):
        self.__state = {'time': 0, 'location': np.array([0, 0])}

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def time(self):
        return self.__state['time']

    @property
    def location(self):
        return self.__state['location']

    def single_move(self): # move for one step
        # draw direction
        pool = [np.array([0, 1]), np.array([0, -1]), np.array([1, 0]), np.array([-1, 0])]
        move = pool[random.randint(0, 3)]
        self.__state['time'] += 1
        self.__state['location'] += self.speed * move        

    def move(self, n_steps):
        for _ in range(n_steps):
            self.single_move()

if __name__ == '__main__':
    a = Ant()
    for i in range(40):
        print(i)
        a.reset()
        a.single_move()
        print(a.time)
        print(a.location)


        
        


    

