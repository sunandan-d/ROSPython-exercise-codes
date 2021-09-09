from Myrobot_control_class import RobotControl

rc = RobotControl()

class OutOfMaze:
    def __init__(self):
        print("Started the Game")


    def turtle_mov(self):
        i=0
        while (i<2):
            self.turtle_straight()
            self.turtle_turn_clock()
            i=i+1

        j=0
        while (j<1):
            self.turtle_straight()
            self.turtle_turn_cclock()
            j=j+1

        laser1 = rc.get_laser(0)
        laser2 = rc.get_laser(719)

        if (laser1 == inf)&&(laser2 == inf):   # The robot is outside the maze
            rc.stop.robot()


    def turtle_straight(self):
        
        laser = rc.get_laser(360)
        print("Laser Start Value")

        while laser>0.8:
            rc.move_straight()
            laser = rc.get_laser(360)
            
        rc.stop_robot()


    def turtle_turn_clock(self):
        rc.rotate(90)

    def turtle_turn_cclock(self):  
        rc.rotate(-90)


ins = OutOfMaze()
ins.turtle_mov()

    
