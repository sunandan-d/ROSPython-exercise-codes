from robot_control_class import RobotControl
import math

def get_highest_lowest():
    rc = RobotControl()
    laser = rc.get_laser_full()

    max = 0
    pos_inf = math.inf
    for x in laser:
        if (x>max)and(x!=pos_inf):
            max = x
    max_index = laser.index(max)
    print("Index of the max value is = ", max_index)

    min = max
    for x in laser:
        if (x<min):
            min = x
    min_index = laser.index(min)
    print("Index of the min value is = ", min_index)

get_highest_lowest()
