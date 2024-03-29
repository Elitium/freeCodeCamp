import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [item for item, number in kwargs.items() for i in range(number)] # creates list of items
    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randint(0, len(self.contents) - 1)) for i in range(n)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    sucess = 0
    for i in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        ballsDrawn = hatCopy.draw(num_balls_drawn)
        goodPass = True
        for item, number in expected_balls.items():
            if ballsDrawn.count(item) < number:
                goodPass = False
                break
        if goodPass == True:
            sucess += 1        
    return sucess/num_experiments
