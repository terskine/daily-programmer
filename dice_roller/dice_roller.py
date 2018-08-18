import random
import sys

def roll(num_die, num_sides):
    return sum([random.randint(1,num_sides) for _ in range(0,num_die)])
    
if __name__== "__main__":
    lines = [line.rstrip('\n') for line in open(sys.argv[1])]
    for x in lines:
        print roll(int(x.split('d')[0]), int(x.split('d')[1]))