import matplotlib as mp
import numpy as np
import csv

def OrthogonalDistance():
    orthogonal_dist_robots = []
    for o in len(robot_odom):
        orthogonal_dist_robots.append(orthogonal_dist)
        orthogonal_dist = []
        for robot_path in robot_paths:
            disp = []   
            for i in len(robot_path):
                disp.append(Pythagoras(robot_odom[o],robot_path[i]))
            min2values = sorted(dist)
            i1 = disp.index(min2values[0])
            i2 = disp.index(min2values[1])

            A = robot_path[i1]
            B = robot_path[i2]
            C = robot_odom[o]

            a = Pythagoras(B,C)
            b = Pythagoras(A,C)
            c = Pythagoras(A,B)
            
            h = 1/(2*c) * np.sqrt(a+b+c) * np.sqrt(-a+b+c) * np.sqrt(a-b+c) * np.sqrt(a+b-c)
            orthogonal_dist.append(h)
            
def Pythagoras(A,B):
    displacement = np.hypot((B[1]-A[1]),(B[0]-A[0]))
    return displacement




